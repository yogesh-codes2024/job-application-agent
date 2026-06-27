import sys
import time
import json
import requests
from sheets import append_new_jobs_to_sheet
from pathlib import Path
from typing import Dict, List
from urllib.parse import quote_plus

from playwright.sync_api import sync_playwright

sys.path.append(str(Path(__file__).resolve().parent))

from sources import COMPANIES, TARGET_TITLES, TARGET_LOCATIONS
from normalize import normalize_job, title_matches, location_matches
from dedupe import merge_jobs
from sheets import append_new_jobs_to_sheet


def request_json(url: str, timeout: int = 30):
    headers = {
        "User-Agent": "Mozilla/5.0 job-discovery-agent/1.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"[WARN] Request failed: {url} | {e}")
        return None


def discover_greenhouse(company: Dict) -> List[Dict]:
    board_token = company["board_token"]
    url = f"https://boards-api.greenhouse.io/v1/boards/{board_token}/jobs?content=true"

    data = request_json(url)
    if not data:
        return []

    jobs = []

    for item in data.get("jobs", []):
        location = item.get("location", {}).get("name", "")
        title = item.get("title", "")
        absolute_url = item.get("absolute_url", "")

        jobs.append({
            "company": company["name"],
            "title": title,
            "location": location,
            "url": absolute_url,
            "source": "greenhouse",
            "job_id": str(item.get("id", absolute_url))
        })

    return jobs


def discover_ashby(company: Dict) -> List[Dict]:
    board_token = company["board_token"]
    url = f"https://api.ashbyhq.com/posting-api/job-board/{board_token}"

    data = request_json(url)
    if not data:
        return []

    jobs = []

    for item in data.get("jobs", []):
        title = item.get("title", "")
        location = item.get("location", "")
        job_id = item.get("id", "")
        job_url = f"https://jobs.ashbyhq.com/{board_token}/{job_id}"

        jobs.append({
            "company": company["name"],
            "title": title,
            "location": location,
            "url": job_url,
            "source": "ashby",
            "job_id": str(job_id)
        })

    return jobs


def discover_smartrecruiters(company: Dict) -> List[Dict]:
    company_id = company["company_id"]
    url = f"https://api.smartrecruiters.com/v1/companies/{company_id}/postings?limit=100"

    data = request_json(url)
    if not data:
        return []

    jobs = []

    for item in data.get("content", []):
        title = item.get("name", "")
        location_obj = item.get("location", {}) or {}
        location = location_obj.get("city", "") or location_obj.get("region", "") or location_obj.get("country", "")
        job_url = item.get("ref", "") or item.get("releasedDate", "")
        job_id = item.get("id", "")

        if not job_url and job_id:
            job_url = f"https://jobs.smartrecruiters.com/{company_id}/{job_id}"

        jobs.append({
            "company": company["name"],
            "title": title,
            "location": location,
            "url": job_url,
            "source": "smartrecruiters",
            "job_id": str(job_id)
        })

    return jobs


def discover_browser_generic(company: Dict) -> List[Dict]:
    """
    Fallback for company pages without simple APIs.
    This opens the careers search page and searches title/location keywords.
    It does not log in, bypass CAPTCHA, or apply.
    """
    jobs = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for title in TARGET_TITLES[:5]:
            search_url = build_search_url(company, title)

            try:
                print(f"[INFO] Browser search: {company['name']} | {title}")
                page.goto(search_url, wait_until="domcontentloaded", timeout=60000)
                page.wait_for_timeout(3000)

                links = page.locator("a").evaluate_all("""
                    els => els.map(a => ({
                        text: a.innerText,
                        href: a.href
                    })).filter(x =>
                        x.href &&
                        x.text &&
                        x.text.length > 5
                    )
                """)

                for link in links:
                    text = link.get("text", "")
                    href = link.get("href", "")

                    if not href:
                        continue

                    if title_matches(text, TARGET_TITLES):
                        jobs.append({
                            "company": company["name"],
                            "title": text,
                            "location": "Unknown",
                            "url": href,
                            "source": company["type"],
                            "job_id": href
                        })

                time.sleep(1)

            except Exception as e:
                print(f"[WARN] Browser discovery failed for {company['name']}: {e}")
                continue

        browser.close()

    return jobs


def build_search_url(company: Dict, title: str) -> str:
    encoded_title = quote_plus(title)

    company_type = company["type"]
    base_url = company["base_url"]

    if company_type == "amazon":
        return f"{base_url}?base_query={encoded_title}&loc_query=Seattle%2C%20WA"

    if company_type == "microsoft":
        return f"{base_url}?q={encoded_title}&lc=United%20States"

    if company_type == "google":
        return f"{base_url}?q={encoded_title}&location=United%20States"

    if company_type == "meta":
        return f"{base_url}?q={encoded_title}"

    if company_type == "apple":
        return f"{base_url}?search={encoded_title}&location=united-states-USA"

    if company_type == "stripe":
        return f"{base_url}?query={encoded_title}&office_locations=North%20America--United%20States"

    if company_type == "salesforce":
        return f"{base_url}?search={encoded_title}"

    if company_type == "oracle":
        return f"{base_url}?keyword={encoded_title}"

    if company_type == "bytedance":
        return f"{base_url}?keyword={encoded_title}&location=CT_157"

    return base_url


def discover_company(company: Dict) -> List[Dict]:
    source_type = company["type"]

    print(f"[INFO] Discovering jobs for {company['name']} via {source_type}")

    if source_type == "greenhouse":
        return discover_greenhouse(company)

    if source_type == "ashby":
        return discover_ashby(company)

    if source_type == "smartrecruiters":
        return discover_smartrecruiters(company)

    return discover_browser_generic(company)


def filter_jobs(raw_jobs: List[Dict]) -> List[Dict]:
    filtered = []

    for raw in raw_jobs:
        job = normalize_job(raw)

        if not job["title"] or not job["url"]:
            continue

        if not title_matches(job["title"], TARGET_TITLES):
            continue

        # If location is unknown from browser fallback, keep it for manual review.
        if job["location"] != "Unknown":
            if not location_matches(job["location"], TARGET_LOCATIONS):
                continue

        filtered.append(job)

    return filtered


def main():
    total_matching = 0
    total_added_csv = 0
    total_added_sheet = 0

    for company in COMPANIES:
        try:
            raw_jobs = discover_company(company)
            filtered = filter_jobs(raw_jobs)

            print(f"[INFO] {company['name']}: {len(filtered)} matching jobs")

            if filtered:
                added_csv = merge_jobs(filtered)
                added_sheet = append_new_jobs_to_sheet(filtered)

                total_added_csv += added_csv
                total_added_sheet += added_sheet
                total_matching += len(filtered)

                print(f"[SAVED] {company['name']}: {added_csv} new jobs added to jobs.csv")
                print(f"[SHEETS] {company['name']}: {added_sheet} new jobs added to Google Sheets")

            time.sleep(2)

        except KeyboardInterrupt:
            print("")
            print("[STOPPED] Interrupted by user. Jobs found before this point were already saved.")
            break

        except Exception as e:
            print(f"[ERROR] Failed company {company['name']}: {e}")
            continue

    print("")
    print(f"[DONE] Matching jobs found this run: {total_matching}")
    print(f"[DONE] New jobs added to jobs.csv: {total_added_csv}")
    print(f"[DONE] New jobs added to Google Sheets: {total_added_sheet}")

if __name__ == "__main__":
    main()