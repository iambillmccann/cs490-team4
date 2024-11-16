from backend.resume_upload.resume_upload import resume_router
from fastapi import FastAPI

app = FastAPI()
app.include_router(resume_router)
