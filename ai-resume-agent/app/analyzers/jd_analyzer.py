import re

SKILLS = [
    "Python",
    "Java",
    "C++",
    "SQL",
    "MongoDB",
    "FastAPI",
    "Flask",
    "Django",
    "React",
    "Node.js",
    "JavaScript",
    "TypeScript",
    "AWS",
    "Docker",
    "Kubernetes",
    "Git",
    "Data Structures",
    "Algorithms",
    "Machine Learning",
    "Deep Learning"
]

ROLES = [
    "Software Engineer",
    "Software Engineering Intern",
    "SDE Intern",
    "Backend Developer",
    "Frontend Developer",
    "Full Stack Developer",
    "Machine Learning Engineer",
    "Data Scientist"
]

COMPANIES = [
    "Google",
    "Amazon",
    "Microsoft",
    "Meta",
    "Netflix",
    "Adobe",
    "Oracle",
    "Salesforce",
    "Uber",
    "Goodyear",
    "OpenAI",
    "NVIDIA",
    "Intel",
    "Apple"
]


def analyze_jd(job_description):

    found_skills = []

    for skill in SKILLS:

        if skill.lower() in job_description.lower():
            found_skills.append(skill)

    role = "Unknown"

    matching_roles = []

    for role_name in ROLES:

        if role_name.lower() in job_description.lower():
            matching_roles.append(role_name)

    if matching_roles:

        role = max(
            matching_roles,
            key=len
        )
    else:
        role = "Unknown"

    company = "Unknown"

    for company_name in COMPANIES:

        if company_name.lower() in job_description.lower():
            company = company_name
            break

    return {
        "company": company,
        "role": role,
        "required_skills": found_skills
    }