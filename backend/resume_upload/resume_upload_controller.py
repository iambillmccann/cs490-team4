from pydantic import BaseModel
from backend.models.enums import *
from PyPDF2 import PdfReader
from io import BytesIO


class JobDescriptionPayload(BaseModel):
    job_description: str


class UploadResponse(BaseModel):
    message: str
    status: str


def validate_job_description(job_description: JobDescriptionPayload):
    if len(job_description.job_description) > 5000:
        return UploadResponse(message=ResumeUploadMessages.JobDescriptionUploadFailure, status=Status.Error)
    return UploadResponse(message=ResumeUploadMessages.JobDescriptionUploadSuccess, status=Status.Success)


def parse_pdf(pdf_file: bytes):
    try:
        pdf_file_bytes = BytesIO(pdf_file)
        pdf_file_read = PdfReader(pdf_file_bytes)
        file = ""
        for page in pdf_file_read.pages:
            print(page.values())
            for line in page.extract_text().split("\n"):
                file += (line.strip() + "\n")
        return file
    except Exception as e:
        raise ValueError(f"Error processing the PDF: {e}")
