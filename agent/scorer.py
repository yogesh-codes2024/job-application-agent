import json
from typing import Dict, Any


def load_profile(path: str = "profile.json") -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def score_job(job: Dict[str, str], profile: Dict[str, Any]) -> Dict[str, Any]:
    score = 0
    reasons = []

    title = job.get("title", "").lower()
    company = job.get("company", "").lower()
    location = job.get("location", "").lower()

    target_titles = [t.lower() for t in profile["target_titles"]]
    preferred_locations = [l.lower() for l in profile["preferred_locations"]]
    priority_companies = [c.lower() for c in profile["company_priority"]]

    if any(t in title or title in t for t in target_titles):
        score += 30
        reasons.append("Title matches target Software Engineer II / Senior Software Engineer roles.")

    if any(loc in location for loc in preferred_locations):
        score += 25
        reasons.append("Location matches Seattle, Eastside, California, or remote preference.")

    if company in priority_companies:
        score += 25
        reasons.append("Company is on your priority tech-company list.")

    if "senior" in title:
        score += 10
        reasons.append("Senior-level role may better support $180K+ base and equity.")

    if "software engineer ii" in title or "sde ii" in title or "software engineer 2" in title:
        score += 10
        reasons.append("SWE II/SDE II title directly matches your target level.")

    recommendation = "HIGH" if score >= 70 else "MEDIUM" if score >= 45 else "LOW"

    return {
        "score": score,
        "recommendation": recommendation,
        "reasons": reasons
    }