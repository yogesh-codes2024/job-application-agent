import csv
import sys
from pathlib import Path

from rich.console import Console
from rich.table import Table

sys.path.append(str(Path(__file__).resolve().parent))

from scorer import load_profile, score_job
from form_answers import get_standard_answers
from tracker import log_application_review
from browser_apply import prefill_application


console = Console()


def load_jobs(path: str = "jobs.csv"):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def show_jobs(jobs, profile):
    table = Table(title="Job Application Queue")

    table.add_column("#")
    table.add_column("Company")
    table.add_column("Title")
    table.add_column("Location")
    table.add_column("Score")
    table.add_column("Recommendation")

    scored = []

    for idx, job in enumerate(jobs, start=1):
        result = score_job(job, profile)
        scored.append((job, result))

        table.add_row(
            str(idx),
            job.get("company", ""),
            job.get("title", ""),
            job.get("location", ""),
            str(result["score"]),
            result["recommendation"]
        )

    console.print(table)
    return scored


def main():
    profile = load_profile()
    answers = get_standard_answers(profile)
    jobs = load_jobs()

    if not jobs:
        print("No jobs found in jobs.csv")
        return

    scored_jobs = show_jobs(jobs, profile)

    choice = input("\nEnter job number to open and prefill, or 'q' to quit: ").strip()

    if choice.lower() == "q":
        return

    try:
        idx = int(choice) - 1
        job, result = scored_jobs[idx]
    except Exception:
        print("Invalid choice.")
        return

    print("\nSelected job:")
    print(job)

    print("\nFit score:")
    print(result)

    confirm = input("\nOpen this job and attempt prefill? Type YES to continue: ").strip()

    if confirm != "YES":
        log_application_review(job, result, "SKIPPED", "User did not approve opening.")
        return

    prefill_application(job, profile, answers)

    final_status = input("\nStatus? APPLIED / SAVED / BLOCKED / SKIPPED: ").strip().upper()
    notes = input("Notes: ").strip()

    log_application_review(job, result, final_status, notes)

    print("Application tracker updated.")


if __name__ == "__main__":
    main()