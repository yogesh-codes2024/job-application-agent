import os
import json
from datetime import date
from typing import Dict, List, Any

import gspread
from google.oauth2.service_account import Credentials


SHEET_HEADERS = [
    "date_discovered",
    "date_applied",
    "company",
    "role_title",
    "job_link",
    "career_portal",
    "location",
    "work_model",
    "compensation",
    "salary_min",
    "salary_max",
    "equity_available",
    "h1b_likely",
    "sponsorship_required",
    "fit_score",
    "status",
    "application_status",
    "resume_version",
    "portal_type",
    "job_id",
    "source",
    "last_checked",
    "notes",
]


def get_client():
    raw_json = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON")
    if not raw_json:
        raise RuntimeError("Missing GOOGLE_SERVICE_ACCOUNT_JSON environment variable")

    service_account_info = json.loads(raw_json)

    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ]

    credentials = Credentials.from_service_account_info(
        service_account_info,
        scopes=scopes,
    )

    return gspread.authorize(credentials)


def get_jobs_worksheet():
    sheet_name = os.environ.get("GOOGLE_SHEET_NAME")
    if not sheet_name:
        raise RuntimeError("Missing GOOGLE_SHEET_NAME environment variable")

    client = get_client()
    spreadsheet = client.open(sheet_name)

    try:
        worksheet = spreadsheet.worksheet("Jobs")
    except gspread.WorksheetNotFound:
        worksheet = spreadsheet.add_worksheet(
            title="Jobs",
            rows=1000,
            cols=len(SHEET_HEADERS)
        )

    existing = worksheet.row_values(1)

    if existing != SHEET_HEADERS:
        worksheet.clear()
        worksheet.append_row(SHEET_HEADERS)

    return worksheet


def row_key(row: Dict[str, Any]) -> str:
    company = str(row.get("company", "")).strip().lower()
    job_id = str(row.get("job_id", "")).strip().lower()
    job_link = str(row.get("job_link", "")).strip().lower()

    if job_id:
        return f"{company}::{job_id}"

    return f"{company}::{job_link}"


def load_existing_rows(worksheet) -> Dict[str, Dict[str, Any]]:
    records = worksheet.get_all_records()
    existing = {}

    for record in records:
        key = row_key(record)
        if key:
            existing[key] = record

    return existing


def estimate_fit_score(job: Dict[str, Any]) -> int:
    score = 0

    title = job.get("title", "").lower()
    company = job.get("company", "").lower()
    location = job.get("location", "").lower()

    tier_1_companies = [
        "microsoft",
        "google",
        "meta",
        "apple",
        "adobe",
        "nvidia",
        "snowflake",
        "databricks",
        "confluent",
        "stripe",
        "uber",
        "airbnb",
        "doordash",
        "block",
        "coinbase",
        "salesforce",
        "intuit",
        "roblox",
        "pinterest"
    ]

    if "software engineer" in title or "software development engineer" in title:
        score += 30

    if "senior" in title or " ii" in title or " 2" in title or "sde ii" in title:
        score += 20

    if any(x in location for x in [
        "seattle",
        "bellevue",
        "redmond",
        "kirkland",
        "california",
        "san francisco",
        "san jose",
        "sunnyvale",
        "mountain view",
        "palo alto",
        "remote"
    ]):
        score += 25

    if company in tier_1_companies:
        score += 25

    return min(score, 100)


def job_to_sheet_row(job: Dict[str, Any]) -> Dict[str, Any]:
    today = date.today().isoformat()
    fit_score = estimate_fit_score(job)

    status = "HIGH_FIT" if fit_score >= 75 else "NEW"

    return {
        "date_discovered": today,
        "date_applied": "",
        "company": job.get("company", ""),
        "role_title": job.get("title", ""),
        "job_link": job.get("url", ""),
        "career_portal": job.get("career_portal", job.get("url", "")),
        "location": job.get("location", ""),
        "work_model": job.get("work_model", ""),
        "compensation": job.get("compensation", ""),
        "salary_min": job.get("salary_min", ""),
        "salary_max": job.get("salary_max", ""),
        "equity_available": job.get("equity_available", ""),
        "h1b_likely": job.get("h1b_likely", ""),
        "sponsorship_required": "Yes",
        "fit_score": fit_score,
        "status": status,
        "application_status": "NOT_STARTED",
        "resume_version": "Yogesh_Narigapalli_Resume.pdf",
        "portal_type": job.get("source", ""),
        "job_id": job.get("job_id", ""),
        "source": job.get("source", ""),
        "last_checked": today,
        "notes": "",
    }


def append_new_jobs_to_sheet(jobs: List[Dict[str, Any]]) -> int:
    worksheet = get_jobs_worksheet()
    existing = load_existing_rows(worksheet)

    rows_to_append = []

    for job in jobs:
        sheet_row = job_to_sheet_row(job)
        key = row_key(sheet_row)

        if key in existing:
            continue

        rows_to_append.append([sheet_row.get(header, "") for header in SHEET_HEADERS])

    if rows_to_append:
        worksheet.append_rows(rows_to_append, value_input_option="USER_ENTERED")

    return len(rows_to_append)