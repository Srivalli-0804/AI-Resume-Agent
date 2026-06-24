from bson import ObjectId

from app.database.mongodb import db

master_resumes_collection = db["master_resumes"]


def get_master_resume(
    resume_id
):

    document = master_resumes_collection.find_one(
        {
            "_id": ObjectId(
                resume_id
            )
        }
    )

    return document