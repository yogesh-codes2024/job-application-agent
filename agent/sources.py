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
        "name": "Adobe",
        "type": "workday",
        "base_url": "https://adobe.wd5.myworkdayjobs.com/external_experienced"
    },
    {
        "name": "Nvidia",
        "type": "workday",
        "base_url": "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite"
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
        "name": "Salesforce",
        "type": "salesforce",
        "base_url": "https://careers.salesforce.com/en/jobs/"
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
    },
    {
        "name": "LinkedIn",
        "type": "microsoft",
        "base_url": "https://jobs.careers.microsoft.com/global/en/search"
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
        "name": "Oracle",
        "type": "oracle",
        "base_url": "https://careers.oracle.com/jobs/"
    },
    {
        "name": "ServiceNow",
        "type": "servicenow",
        "base_url": "https://careers.servicenow.com/jobs"
    },
    {
        "name": "PayPal",
        "type": "workday",
        "base_url": "https://paypal.wd1.myworkdayjobs.com/jobs"
    },
    {
        "name": "Visa",
        "type": "smartrecruiters",
        "company_id": "Visa",
        "base_url": "https://jobs.smartrecruiters.com/Visa"
    },
    {
        "name": "Mastercard",
        "type": "workday",
        "base_url": "https://mastercard.wd1.myworkdayjobs.com/CorporateCareers"
    },
    {
        "name": "Capital One",
        "type": "capitalone",
        "base_url": "https://www.capitalonecareers.com/search-jobs"
    },
    {
        "name": "JPMorgan Chase",
        "type": "jpmorgan",
        "base_url": "https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/requisitions"
    },
    {
        "name": "Walmart Global Tech",
        "type": "workday",
        "base_url": "https://walmart.wd5.myworkdayjobs.com/WalmartExternal"
    },
    {
        "name": "Expedia Group",
        "type": "workday",
        "base_url": "https://expedia.wd5.myworkdayjobs.com/search"
    },
    {
        "name": "Zillow",
        "type": "greenhouse",
        "board_token": "zillow",
        "base_url": "https://boards.greenhouse.io/zillow"
    },
    {
        "name": "Dropbox",
        "type": "greenhouse",
        "board_token": "dropbox",
        "base_url": "https://boards.greenhouse.io/dropbox"
    },
    {
        "name": "Box",
        "type": "greenhouse",
        "board_token": "box",
        "base_url": "https://boards.greenhouse.io/box"
    },
    {
        "name": "Atlassian",
        "type": "greenhouse",
        "board_token": "atlassian",
        "base_url": "https://boards.greenhouse.io/atlassian"
    },
    {
        "name": "GitHub",
        "type": "github",
        "base_url": "https://www.github.careers/careers-home/jobs"
    },
    {
        "name": "GitLab",
        "type": "greenhouse",
        "board_token": "gitlab",
        "base_url": "https://boards.greenhouse.io/gitlab"
    },
    {
        "name": "MongoDB",
        "type": "greenhouse",
        "board_token": "mongodb",
        "base_url": "https://boards.greenhouse.io/mongodb"
    },
    {
        "name": "Elastic",
        "type": "greenhouse",
        "board_token": "elastic",
        "base_url": "https://boards.greenhouse.io/elastic"
    },
    {
        "name": "HashiCorp",
        "type": "greenhouse",
        "board_token": "hashicorp",
        "base_url": "https://boards.greenhouse.io/hashicorp"
    },
    {
        "name": "Cloudflare",
        "type": "greenhouse",
        "board_token": "cloudflare",
        "base_url": "https://boards.greenhouse.io/cloudflare"
    },
    {
        "name": "Twilio",
        "type": "greenhouse",
        "board_token": "twilio",
        "base_url": "https://boards.greenhouse.io/twilio"
    },
    {
        "name": "Okta",
        "type": "greenhouse",
        "board_token": "okta",
        "base_url": "https://boards.greenhouse.io/okta"
    },
    {
        "name": "Workday",
        "type": "workday",
        "base_url": "https://workday.wd5.myworkdayjobs.com/Workday"
    },
    {
        "name": "Splunk",
        "type": "splunk",
        "base_url": "https://www.splunk.com/en_us/careers/search-jobs.html"
    },
    {
        "name": "Cisco",
        "type": "cisco",
        "base_url": "https://jobs.cisco.com/jobs/SearchJobs"
    },
    {
        "name": "AMD",
        "type": "workday",
        "base_url": "https://amd.wd1.myworkdayjobs.com/AMDcareers"
    },
    {
        "name": "Qualcomm",
        "type": "workday",
        "base_url": "https://qualcomm.wd5.myworkdayjobs.com/External"
    },
    {
        "name": "Palantir",
        "type": "greenhouse",
        "board_token": "palantir",
        "base_url": "https://boards.greenhouse.io/palantir"
    },
    {
        "name": "Figma",
        "type": "greenhouse",
        "board_token": "figma",
        "base_url": "https://boards.greenhouse.io/figma"
    },
    {
        "name": "Rippling",
        "type": "ashby",
        "board_token": "rippling",
        "base_url": "https://jobs.ashbyhq.com/rippling"
    },
    {
        "name": "Plaid",
        "type": "greenhouse",
        "board_token": "plaid",
        "base_url": "https://boards.greenhouse.io/plaid"
    },
    {
        "name": "Instacart",
        "type": "greenhouse",
        "board_token": "instacart",
        "base_url": "https://boards.greenhouse.io/instacart"
    },
    {
        "name": "Lyft",
        "type": "greenhouse",
        "board_token": "lyft",
        "base_url": "https://boards.greenhouse.io/lyft"
    },
    {
        "name": "Reddit",
        "type": "greenhouse",
        "board_token": "reddit",
        "base_url": "https://boards.greenhouse.io/reddit"
    },
    {
        "name": "Affirm",
        "type": "greenhouse",
        "board_token": "affirm",
        "base_url": "https://boards.greenhouse.io/affirm"
    },
    {
        "name": "SoFi",
        "type": "greenhouse",
        "board_token": "sofi",
        "base_url": "https://boards.greenhouse.io/sofi"
    },
    {
        "name": "Chime",
        "type": "greenhouse",
        "board_token": "chime",
        "base_url": "https://boards.greenhouse.io/chime"
    },
    {
        "name": "Brex",
        "type": "greenhouse",
        "board_token": "brex",
        "base_url": "https://boards.greenhouse.io/brex"
    },
    {
        "name": "Ramp",
        "type": "greenhouse",
        "board_token": "ramp",
        "base_url": "https://boards.greenhouse.io/ramp"
    }
]