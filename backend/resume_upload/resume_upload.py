from fastapi import APIRouter
from backend.resume_upload.resume_upload_controller import Resume

resume_router = APIRouter()


@resume_router.post('/resume_upload')
def resume_upload(resume: Resume):
    return 201, 201
