from pydantic import BaseModel


class JobRequest(BaseModel):
    job_url: str
    job_description: str