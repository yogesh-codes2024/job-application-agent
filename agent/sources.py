from typing import List, Dict


TARGET_TITLES = [
    "Software Engineer II",
    "Software Engineer 2",
    "SDE II",
    "Software Development Engineer II",
    "Senior Software Engineer",
    "Backend Software Engineer",
    "Full Stack Software Engineer",
    "Software Engineer, Distributed Systems",
    "Software Engineer, Data Platform",
    "Software Engineer, AI Platform"
]


TARGET_LOCATIONS = [
    "Seattle",
    "Bellevue",
    "Redmond",
    "Kirkland",
    "Washington",
    "California",
    "San Francisco",
    "San Jose",
    "Sunnyvale",
    "Mountain View",
    "Palo Alto",
    "Los Angeles",
    "San Diego",
    "Remote"
]


COMPANIES: List[Dict] = [

    {
        "name": "Microsoft",
        "type": "microsoft",
        "base_url": "https://jobs.careers.microsoft.com/global/en/search"
    },
    {
        "name": "Google",
        "type": "google",
        "base_url": "https://www.google.com/about/careers/applications/jobs/results"
    },
    {
        "name": "Meta",
        "type": "meta",
        "base_url": "https://www.metacareers.com/jobs"
    },
    {
        "name": "Apple",
        "type": "apple",
        "base_url": "https://jobs.apple.com/en-us/search"
    },
    {
        "name": "Snowflake",
        "type": "greenhouse",
        "board_token": "snowflake",
        "base_url": "https://boards.greenhouse.io/snowflake"
    },
    {
        "name": "Databricks",
        "type": "greenhouse",
        "board_token": "databricks",
        "base_url": "https://boards.greenhouse.io/databricks"
    },
    {
        "name": "Confluent",
        "type": "greenhouse",
        "board_token": "confluent",
        "base_url": "https://boards.greenhouse.io/confluent"
    },
    {
        "name": "Stripe",
        "type": "stripe",
        "base_url": "https://stripe.com/jobs/search"
    },
    {
        "name": "Uber",
        "type": "greenhouse",
        "board_token": "uber",
        "base_url": "https://boards.greenhouse.io/uber"
    },
    {
        "name": "Airbnb",
        "type": "greenhouse",
        "board_token": "airbnb",
        "base_url": "https://boards.greenhouse.io/airbnb"
    },
    {
        "name": "DoorDash",
        "type": "greenhouse",
        "board_token": "doordash",
        "base_url": "https://boards.greenhouse.io/doordash"
    },
    {
        "name": "Block",
        "type": "smartrecruiters",
        "company_id": "Square",
        "base_url": "https://jobs.smartrecruiters.com/Square"
    },
    {
        "name": "Coinbase",
        "type": "ashby",
        "board_token": "coinbase",
        "base_url": "https://jobs.ashbyhq.com/coinbase"
    },
    {
        "name": "LinkedIn",
        "type": "microsoft",
        "base_url": "https://jobs.careers.microsoft.com/global/en/search"
    },
    {
        "name": "Nvidia",
        "type": "workday",
        "base_url": "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite"
    },
    {
        "name": "Adobe",
        "type": "workday",
        "base_url": "https://adobe.wd5.myworkdayjobs.com/external_experienced"
    },
    {
        "name": "Salesforce",
        "type": "salesforce",
        "base_url": "https://careers.salesforce.com/en/jobs/"
    },
    {
        "name": "Oracle",
        "type": "oracle",
        "base_url": "https://careers.oracle.com/jobs/"
    },
    {
        "name": "Netflix",
        "type": "greenhouse",
        "board_token": "netflix",
        "base_url": "https://boards.greenhouse.io/netflix"
    },
    {
        "name": "TikTok",
        "type": "bytedance",
        "base_url": "https://careers.tiktok.com/search"
    },
    {
        "name": "Intuit",
        "type": "workday",
        "base_url": "https://intuit.wd5.myworkdayjobs.com/External"
    },
    {
        "name": "Roblox",
        "type": "greenhouse",
        "board_token": "roblox",
        "base_url": "https://boards.greenhouse.io/roblox"
    },
    {
        "name": "Pinterest",
        "type": "greenhouse",
        "board_token": "pinterest",
        "base_url": "https://boards.greenhouse.io/pinterest"
    }
]