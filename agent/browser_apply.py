from pathlib import Path
from typing import Dict, Any
from playwright.sync_api import sync_playwright, Page


def safe_fill(page: Page, selectors: list[str], value: str) -> bool:
    for selector in selectors:
        try:
            locator = page.locator(selector).first
            if locator.count() > 0:
                locator.fill(value)
                return True
        except Exception:
            continue
    return False


def safe_fill_by_label(page: Page, label_text: str, value: str) -> bool:
    try:
        field = page.get_by_label(label_text, exact=False).first
        if field.count() > 0:
            try:
                field.fill(value)
                return True
            except Exception:
                try:
                    field.select_option(label=value)
                    return True
                except Exception:
                    return False
    except Exception:
        return False

    return False


def upload_resume(page: Page, resume_path: str) -> bool:
    path = Path(resume_path)

    if not path.exists():
        print(f"Resume not found: {resume_path}")
        return False

    try:
        file_inputs = page.locator("input[type='file']")
        count = file_inputs.count()

        if count == 0:
            print("No file upload input found.")
            return False

        file_inputs.first.set_input_files(str(path))
        return True

    except Exception as e:
        print(f"Resume upload failed: {e}")
        return False


def prefill_application(
    job: Dict[str, str],
    profile: Dict[str, Any],
    answers: Dict[str, str]
) -> None:
    url = job["url"]

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            slow_mo=200
        )

        context = browser.new_context()
        page = context.new_page()

        print(f"Opening job URL: {url}")
        page.goto(url, wait_until="domcontentloaded", timeout=60000)

        print("Attempting to prefill common fields...")

        safe_fill(page, [
            "input[name='firstName']",
            "input[name='first_name']",
            "input[id*='first']",
            "input[aria-label*='First']"
        ], answers["first_name"])

        safe_fill(page, [
            "input[name='lastName']",
            "input[name='last_name']",
            "input[id*='last']",
            "input[aria-label*='Last']"
        ], answers["last_name"])

        safe_fill(page, [
            "input[type='email']",
            "input[name='email']",
            "input[id*='email']",
            "input[aria-label*='Email']"
        ], answers["email"])

        safe_fill(page, [
            "input[type='tel']",
            "input[name='phone']",
            "input[id*='phone']",
            "input[aria-label*='Phone']"
        ], answers["phone"])

        safe_fill(page, [
            "input[name*='linkedin']",
            "input[id*='linkedin']",
            "input[aria-label*='LinkedIn']"
        ], answers["linkedin"])

        safe_fill_by_label(page, "First Name", answers["first_name"])
        safe_fill_by_label(page, "Last Name", answers["last_name"])
        safe_fill_by_label(page, "Email", answers["email"])
        safe_fill_by_label(page, "Phone", answers["phone"])
        safe_fill_by_label(page, "LinkedIn", answers["linkedin"])
        safe_fill_by_label(page, "Location", answers["location"])

        safe_fill_by_label(page, "Are you legally authorized", answers["authorized_to_work_us"])
        safe_fill_by_label(page, "authorized to work", answers["authorized_to_work_us"])
        safe_fill_by_label(page, "require sponsorship", answers["requires_sponsorship"])
        safe_fill_by_label(page, "sponsorship now or in the future", answers["requires_sponsorship_now_or_future"])
        safe_fill_by_label(page, "visa", answers["visa_status"])
        safe_fill_by_label(page, "salary", answers["salary_expectation"])

        uploaded = upload_resume(page, profile["resume_path"])

        print(f"Resume uploaded: {uploaded}")
        print("")
        print("Manual review required.")
        print("Check all answers carefully.")
        print("Do not submit unless everything is correct.")
        print("Close the browser when finished.")

        page.wait_for_timeout(15 * 60 * 1000)
        browser.close()