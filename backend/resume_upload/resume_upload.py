from fastapi import APIRouter
from pydantic import BaseModel
from backend.resume_upload.resume_upload_modules import Resume
resume_router = APIRouter()


@resume_router.post('/resume_upload')
def resume_upload(resume: Resume):
    return 201
