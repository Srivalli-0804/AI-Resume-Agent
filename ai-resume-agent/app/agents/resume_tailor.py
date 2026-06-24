import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def tailor_resume(
    resume_text,
    job_description,
    missing_skills
):

    prompt = f"""
You are an expert ATS Resume Optimizer.

Resume:
{resume_text}

Job Description:
{job_description}

Missing Skills:
{missing_skills}

Instructions:

1. Rewrite the resume to better match the job description.
2. Improve bullet points.
3. Use ATS-friendly keywords.
4. Maintain truthfulness.
5. Do not invent fake experience.
6. Return only the tailored resume.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content