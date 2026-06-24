from fastapi import FastAPI, UploadFile, File
import os
import shutil
from fastapi.middleware.cors import CORSMiddleware
from app.parsers.resume_parser import parse_resume
from app.models.job_request import JobRequest

from app.analyzers.resume_analyzer import analyze_resume
from app.analyzers.jd_analyzer import analyze_jd
from app.analyzers.skill_matcher import match_skills
from app.analyzers.ats_scorer import calculate_ats_score
from app.analyzers.gap_analyzer import generate_gap_analysis

from app.agents.resume_tailor import tailor_resume

from app.generators.resume_generator import generate_resume_docx

from app.database.mongodb import db
from app.database.resume_store import save_master_resume
from app.database.application_store import save_application
from app.models.process_job_request import ProcessJobRequest
from app.database.resume_retriever import get_master_resume
from app.database.application_store import applications_collection

from app.services.semantic_matcher import semantic_match_score
from app.services.project_matcher import (
    calculate_project_score
)
from app.services.job_recommender import (
    recommend_jobs
)
from app.models.scrape_job_request import (
    ScrapeJobRequest
)
from app.services.linkedin_scraper import (
    scrape_linkedin_job
)

app = FastAPI(
    title="AI Resume Agent",
    version="1.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
UPLOAD_FOLDER = "uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


@app.get("/")
def home():

    return {
        "message": "AI Resume Agent Running Successfully"
    }


@app.get("/test-db")
async def test_db():

    return {
        "database": db.name,
        "status": "connected"
    }


@app.post("/upload-resume")
async def upload_resume(
    resume: UploadFile = File(...)
):

    allowed_types = [
        ".pdf",
        ".docx"
    ]

    extension = os.path.splitext(
        resume.filename
    )[1].lower()

    if extension not in allowed_types:

        return {
            "status": "error",
            "message": "Only PDF and DOCX files are allowed"
        }

    file_path = os.path.join(
        UPLOAD_FOLDER,
        resume.filename
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            resume.file,
            buffer
        )

    resume_text = parse_resume(
        file_path
    )

    resume_analysis = analyze_resume(
        resume_text
    )

    resume_id = save_master_resume(
        resume.filename,
        file_path,
        resume_text,
        resume_analysis
    )

    return {
        "status": "success",
        "resume_id": resume_id,
        "filename": resume.filename,
        "path": file_path,
        "resume_analysis": resume_analysis
    }


@app.post("/job-input")
async def job_input(
    job: JobRequest
):

    analysis = analyze_jd(
        job.job_description
    )

    return {
        "status": "success",
        "job_url": job.job_url,
        "analysis": analysis
    }


@app.post("/skill-match")
async def skill_match():

    resume_skills = [
        "Python",
        "SQL",
        "React",
        "MongoDB"
    ]

    jd_skills = [
        "Python",
        "SQL",
        "FastAPI",
        "Docker"
    ]

    result = match_skills(
        resume_skills,
        jd_skills
    )

    ats_score = calculate_ats_score(
        result["matched"],
        jd_skills
    )

    gap_analysis = generate_gap_analysis(
        result["missing"]
    )

    return {
        "ats_score": ats_score,
        "matched": result["matched"],
        "missing_skills": gap_analysis["missing_skills"],
        "recommendations": gap_analysis["recommendations"]
    }


@app.post("/tailor-resume")
async def tailor_resume_test():

    sample_resume = """
Computer Science Student

Skills:
Python
SQL
React

Projects:
Expense Tracker using MERN Stack
"""

    sample_jd = """
Software Engineering Intern

Requirements:
Python
SQL
FastAPI
Docker
REST APIs
"""

    missing_skills = [
        "FastAPI",
        "Docker"
    ]

    tailored_resume = tailor_resume(
        sample_resume,
        sample_jd,
        missing_skills
    )

    return {
        "tailored_resume": tailored_resume
    }


@app.post("/generate-resume")
async def generate_resume():

    sample_resume = """
Computer Science Student

Skills:
Python
SQL
React

Projects:
Expense Tracker using MERN Stack
"""

    sample_jd = """
Software Engineering Intern

Requirements:
Python
SQL
FastAPI
Docker
REST APIs
"""

    missing_skills = [
        "FastAPI",
        "Docker"
    ]

    tailored_resume = tailor_resume(
        sample_resume,
        sample_jd,
        missing_skills
    )

    file_path = generate_resume_docx(
        tailored_resume,
        "Google_SWE_Resume.docx"
    )

    return {
        "message": "Resume generated successfully",
        "file_path": file_path
    }


@app.post("/process-job")
async def process_job(
    request: ProcessJobRequest
):

    # Get master resume from MongoDB
    resume_document = get_master_resume(
        request.resume_id
    )

    if not resume_document:

        return {
            "status": "error",
            "message": "Resume not found"
        }

    # Resume skills
    resume_skills = resume_document[
        "resume_analysis"
    ]["skills"]

    # Full resume text
    resume_text = resume_document.get(
        "resume_text",
        ""
    )

    # Analyze JD
    jd_analysis = analyze_jd(
        request.job_description
    )

    jd_skills = jd_analysis[
        "required_skills"
    ]

    # Skill Matching
    match_result = match_skills(
        resume_skills,
        jd_skills
    )

    # ATS Score
    ats_score = calculate_ats_score(
        match_result["matched"],
        jd_skills
    )
    
    semantic_score = semantic_match_score(
        resume_text,
        request.job_description
    )

    project_score = calculate_project_score(
        resume_document["resume_analysis"].get(
            "projects",
            ""
        ),
    request.job_description
    )

    final_ats_score = round(

    (
        ats_score * 0.3
        +
        semantic_score * 0.4
        +
        project_score * 0.3
    ),

    2
)
    
    # Gap Analysis
    gap_analysis = generate_gap_analysis(
        match_result["missing"]
    )

    # Tailor Resume using actual resume text
    tailored_resume = tailor_resume(
        resume_text,
        request.job_description,
        match_result["missing"]
    )

    # Generate Resume File
    generated_file = generate_resume_docx(
        tailored_resume,
        jd_analysis["company"],
        jd_analysis["role"]
)

    # Store Application
    application_id = save_application(
        company=jd_analysis["company"],
        role=jd_analysis["role"],
        job_url=request.job_url,
        ats_score=final_ats_score,
        matched_skills=match_result["matched"],
        missing_skills=match_result["missing"],
        resume_file=generated_file
)
    return {

        "status": "success",

        "company": jd_analysis["company"],

        "application_id": application_id,

        "job_url": request.job_url,

        "role": jd_analysis["role"],

        "ats_score": final_ats_score,

        "keyword_ats_score": ats_score,

        "semantic_ats_score": semantic_score,

        "project_score": project_score,

        "matched_skills":
            match_result["matched"],

        "missing_skills":
            match_result["missing"],

        "recommendations":
            gap_analysis["recommendations"],

        "generated_resume":
            generated_file
    }


@app.get("/applications")
async def get_applications():

    applications = list(
        applications_collection.find(
            {},
            {"_id": 0}
        )
    )

    return applications

@app.get("/recommend-jobs/{resume_id}")
async def get_job_recommendations(
    resume_id: str
):

    resume_document = get_master_resume(
        resume_id
    )

    if not resume_document:

        return {
            "status": "error",
            "message": "Resume not found"
        }

    skills = resume_document[
        "resume_analysis"
    ]["skills"]

    recommendations = recommend_jobs(
        skills
    )

    return {
        "status": "success",
        "recommendations":
            recommendations
    }


@app.post("/scrape-job")
async def scrape_job(
    request: ScrapeJobRequest
):

    try:

        result = await scrape_linkedin_job(
            request.job_url
        )

        return {
            "status": "success",
            "title": result["title"],
            "description": result["description"]
        }

    except Exception as e:

        import traceback

        return {
            "status": "error",
            "message": repr(e),
            "traceback": traceback.format_exc()
        }