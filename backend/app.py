from backend.user_signup.user_signup import signup_router
from backend.resume_upload.resume_upload import resume_router
from fastapi import FastAPI

app = FastAPI()
app.include_router(signup_router)
app.include_router(user_router)