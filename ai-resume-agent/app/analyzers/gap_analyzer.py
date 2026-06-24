def generate_gap_analysis(
    missing_skills
):

    recommendations = []

    skill_recommendations = {

        "FastAPI":
            "Highlight backend API projects",

        "Flask":
            "Mention web service development",

        "Docker":
            "Mention deployment or containerization experience",

        "AWS":
            "Highlight cloud-related projects",

        "Kubernetes":
            "Mention orchestration or deployment experience",

        "React":
            "Highlight frontend development projects",

        "MongoDB":
            "Mention database implementation experience",

        "Machine Learning":
            "Highlight ML projects and coursework",

        "Deep Learning":
            "Showcase neural network projects",

        "Data Structures":
            "Emphasize coding problem-solving experience",

        "Algorithms":
            "Highlight competitive programming or DSA projects"
    }

    for skill in missing_skills:

        if skill in skill_recommendations:

            recommendations.append(
                skill_recommendations[skill]
            )

    if not recommendations:

        recommendations.append(
            "Resume already aligns well with job requirements"
        )

    return {
        "missing_skills": missing_skills,
        "recommendations": recommendations
    }