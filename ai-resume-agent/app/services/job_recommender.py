ROLE_SKILL_MAP = {

    "Software Engineer Intern": [
        "Python",
        "Java",
        "SQL",
        "Algorithms",
        "Data Structures"
    ],

    "Backend Developer": [
        "Python",
        "FastAPI",
        "Flask",
        "SQL",
        "MongoDB"
    ],

    "Frontend Developer": [
        "React",
        "JavaScript",
        "TypeScript"
    ],

    "Full Stack Developer": [
        "React",
        "Node.js",
        "MongoDB",
        "JavaScript"
    ],

    "Machine Learning Engineer": [
        "Python",
        "Machine Learning",
        "Deep Learning"
    ],

    "Data Scientist": [
        "Python",
        "SQL",
        "Machine Learning"
    ]
}


def recommend_jobs(resume_skills):

    recommendations = []

    for role, skills in ROLE_SKILL_MAP.items():

        matched = len(

            set(resume_skills)

            &

            set(skills)

        )

        score = round(

            matched /
            len(skills)
            * 100,

            2
        )

        recommendations.append({

            "role": role,

            "match_score": score
        })

    recommendations.sort(

        key=lambda x:
        x["match_score"],

        reverse=True
    )

    return recommendations[:5]