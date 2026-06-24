def calculate_ats_score(
    matched_skills,
    jd_skills
):

    if len(jd_skills) == 0:
        score = 0

    else:
        score = (
            len(matched_skills)
            / len(jd_skills)
        ) * 100

    return round(score, 2)