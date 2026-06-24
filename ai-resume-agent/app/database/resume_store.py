from app.database.mongodb import db

master_resumes_collection = db["master_resumes"]


def save_master_resume(
    filename,
    file_path,
    resume_text,
    resume_analysis
):

    document = {

        "filename": filename,

        "file_path": file_path,

        "resume_text": resume_text,

        "resume_analysis": resume_analysis
    }

    result = master_resumes_collection.insert_one(
        document
    )

    return str(
        result.inserted_id
    )