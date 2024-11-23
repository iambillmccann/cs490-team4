from pydantic import BaseModel
from backend.models.enums import *


class JobDescriptionPayload(BaseModel):
    job_description: str


class UploadResponse(BaseModel):
    message: str
    status: str


def validate_job_description(job_description: JobDescriptionPayload):
    if len(job_description.job_description) > 5000:
        return UploadResponse(message=ResumeUploadMessages.JobDescriptionUploadFailure, status=Status.Error)
    return UploadResponse(message=ResumeUploadMessages.JobDescriptionUploadSuccess, status=Status.Success)