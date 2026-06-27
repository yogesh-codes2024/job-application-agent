import re
from typing import Dict, List


def clean_text(value: str) -> str:
    if not value:
        return ""
    return re.sub(r"\s+", " ", value).strip()


def title_matches(title: str, target_titles: List[str]) -> bool:
    title_lower = title.lower()

    positive_patterns = [
        "software engineer ii",
        "software engineer 2",
        "sde ii",
        "software development engineer ii",
        "senior software engineer",
        "backend software engineer",
        "full stack software engineer",
        "distributed systems",
        "data platform",
        "ai platform",
        "machine learning platform",
        "infrastructure engineer",
        "cloud infrastructure"
    ]

    negative_patterns = [
        "intern",
        "internship",
        "new grad",
        "university grad",
        "apprentice",
        "manager",
        "director",
        "principal",
        "staff",
        "frontend only",
        "qa engineer",
        "test engineer",
        "support engineer"
    ]

    if any(pattern in title_lower for pattern in negative_patterns):
        return False

    return any(pattern in title_lower for pattern in positive_patterns)


def location_matches(location: str, target_locations: List[str]) -> bool:
    location_lower = location.lower()

    positive_patterns = [
        "seattle",
        "bellevue",
        "redmond",
        "kirkland",
        "washington",
        "wa",
        "california",
        "ca",
        "san francisco",
        "san jose",
        "sunnyvale",
        "mountain view",
        "palo alto",
        "los angeles",
        "san diego",
        "remote",
        "united states"
    ]

    return any(pattern in location_lower for pattern in positive_patterns)


def normalize_job(raw: Dict) -> Dict:
    return {
        "company": clean_text(raw.get("company", "")),
        "title": clean_text(raw.get("title", "")),
        "location": clean_text(raw.get("location", "")),
        "url": clean_text(raw.get("url", "")),
        "source": clean_text(raw.get("source", "")),
        "job_id": clean_text(raw.get("job_id", raw.get("url", "")))
    }