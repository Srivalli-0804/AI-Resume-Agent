from app.services.semantic_matcher import (
    semantic_match_score
)


def calculate_project_score(
    projects_text,
    job_description
):

    if not projects_text:

        return 0

    return semantic_match_score(
        projects_text,
        job_description
    )