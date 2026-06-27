import csv
from pathlib import Path
from datetime import date
from typing import Dict, List


JOBS_CSV = Path("jobs.csv")


def ensure_jobs_csv() -> None:
    if not JOBS_CSV.exists():
        with JOBS_CSV.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=[
                    "company",
                    "title",
                    "location",
                    "url",
                    "source",
                    "job_id",
                    "first_seen",
                    "last_seen",
                    "status"
                ]
            )
            writer.writeheader()


def load_existing_jobs() -> List[Dict]:
    ensure_jobs_csv()

    with JOBS_CSV.open("r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def job_key(job: Dict) -> str:
    if job.get("job_id"):
        return f"{job.get('company', '').lower()}::{job.get('job_id', '').lower()}"

    return f"{job.get('company', '').lower()}::{job.get('title', '').lower()}::{job.get('location', '').lower()}::{job.get('url', '').lower()}"


def merge_jobs(new_jobs: List[Dict]) -> int:
    today = date.today().isoformat()

    existing = load_existing_jobs()
    existing_by_key = {job_key(job): job for job in existing}

    added_count = 0

    for job in new_jobs:
        key = job_key(job)

        if key in existing_by_key:
            existing_by_key[key]["last_seen"] = today
        else:
            job["first_seen"] = today
            job["last_seen"] = today
            job["status"] = "NEW"
            existing_by_key[key] = job
            added_count += 1

    merged = list(existing_by_key.values())

    with JOBS_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "company",
                "title",
                "location",
                "url",
                "source",
                "job_id",
                "first_seen",
                "last_seen",
                "status"
            ]
        )
        writer.writeheader()
        writer.writerows(merged)

    return added_count