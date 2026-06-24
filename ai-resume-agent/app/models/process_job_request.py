from pydantic import BaseModel


class ProcessJobRequest(BaseModel):

    resume_id: str

    job_url: str

    job_description: str