from pydantic import BaseModel


class ScrapeJobRequest(
    BaseModel
):

    job_url: str