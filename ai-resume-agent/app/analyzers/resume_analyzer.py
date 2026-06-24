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


def extract_section(
    text,
    section_names
):

    lines = text.split("\n")

    collected = []

    capture = False

    for line in lines:

        stripped = line.strip()

        if any(
            section.lower() in stripped.lower()
            for section in section_names
        ):
            capture = True
            continue

        if capture:

            if (
                len(stripped) > 0
                and len(stripped.split()) <= 3
            ):
                break

            collected.append(stripped)

    return "\n".join(collected)


def analyze_resume(
    resume_text
):

    found_skills = []

    for skill in SKILLS:

        if skill.lower() in resume_text.lower():

            found_skills.append(skill)

    projects = extract_section(
        resume_text,
        [
            "Projects",
            "Project"
        ]
    )

    experience = extract_section(
        resume_text,
        [
            "Experience",
            "Work Experience",
            "Internship"
        ]
    )

    education = extract_section(
        resume_text,
        [
            "Education",
            "Academic Background"
        ]
    )

    return {

        "skills": found_skills,

        "projects": projects,

        "experience": experience,

        "education": education
    }