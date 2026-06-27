from typing import Dict, Any


def get_standard_answers(profile: Dict[str, Any]) -> Dict[str, str]:
    return {
        "first_name": profile["first_name"],
        "last_name": profile["last_name"],
        "full_name": profile["name"],
        "email": profile["email"],
        "phone": profile["phone"],
        "location": profile["location"],
        "linkedin": profile["linkedin"],

        "authorized_to_work_us": "Yes",
        "requires_sponsorship": "Yes",
        "requires_sponsorship_now_or_future": "Yes",
        "visa_status": "H1B",

        "desired_salary": str(profile["minimum_base_salary"]),
        "salary_expectation": (
            "My target base salary is $180,000+, with equity or stock compensation "
            "depending on the complete compensation package and role scope."
        ),

        "work_preference": (
            "I am open to Seattle, Bellevue, Redmond, Kirkland, California, and remote roles."
        ),

        "why_interested": (
            "I am interested in this role because it aligns with my background building "
            "distributed systems, cloud-native applications, full-stack platforms, and "
            "data-driven products at companies including AWS and GEICO. I have experience "
            "with Java, Python, React, TypeScript, AWS, Kafka, Flink, Snowflake, REST APIs, "
            "GraphQL, and microservices architecture."
        )
    }