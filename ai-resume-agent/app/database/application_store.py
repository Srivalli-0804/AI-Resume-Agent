from datetime import datetime

from app.database.mongodb import db

applications_collection = db["applications"]


def save_application(
    company,
    role,
    job_url,
    ats_score,
    matched_skills,
    missing_skills,
    resume_file
):

    document = {

        "company": company,

        "role": role,

        "job_url": job_url,

        "ats_score": ats_score,

        "matched_skills": matched_skills,

        "missing_skills": missing_skills,

        "resume_file": resume_file,

        "created_at": datetime.utcnow()
    }

    result = applications_collection.insert_one(
        document
    )

    return str(
        result.inserted_id
    )