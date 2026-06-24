def match_skills(
    resume_skills,
    jd_skills
):

    resume_set = set(
        skill.lower()
        for skill in resume_skills
    )

    jd_set = set(
        skill.lower()
        for skill in jd_skills
    )

    matched = []

    missing = []

    for skill in jd_skills:

        if skill.lower() in resume_set:
            matched.append(skill)

        else:
            missing.append(skill)

    if len(jd_skills) > 0:

        match_percentage = (
            len(matched)
            / len(jd_skills)
        ) * 100

    else:

        match_percentage = 0

    return {
        "matched": matched,
        "missing": missing,
        "match_percentage": round(
            match_percentage,
            2
        )
    }