import csv
from datetime import datetime
from pathlib import Path
from typing import Dict, Any


TRACKER_FILE = Path("applications.csv")


def init_tracker() -> None:
    if not TRACKER_FILE.exists():
        with TRACKER_FILE.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                "date",
                "company",
                "title",
                "location",
                "url",
                "score",
                "recommendation",
                "status",
                "notes"
            ])


def log_application_review(
    job: Dict[str, str],
    score_result: Dict[str, Any],
    status: str,
    notes: str = ""
) -> None:
    init_tracker()

    with TRACKER_FILE.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M"),
            job.get("company", ""),
            job.get("title", ""),
            job.get("location", ""),
            job.get("url", ""),
            score_result.get("score", ""),
            score_result.get("recommendation", ""),
            status,
            notes
        ])