from backend.app import app
from fastapi.testclient import TestClient
from io import BytesIO
from backend.resume_upload.resume_upload_controller import UploadResponse, JobDescriptionPayload


class TestApiBaseClient(TestClient):
    def __init__(self):
        super().__init__(app)

    def url(self, postfix):
        return f'/api/{postfix}'

    def upload_resume(self, file, content_type: bytes | str = 'application/pdf', file_name="test_resume.pdf"):
        if isinstance(file, bytes):
            url = self.url('resume-upload')
            payload = {"resume_file": (file_name, BytesIO(file), content_type)}
            response = self.post(url, files=payload)
            return UploadResponse(**response.json())
        return

    def upload_job_description(self, payload: dict | JobDescriptionPayload) -> UploadResponse:
        if isinstance(payload, JobDescriptionPayload):
            url = self.url('job-description')
            response = self.post(url, json=payload.model_dump())
            return UploadResponse(**response.json())
        elif isinstance(payload, dict):
            url = self.url('job-description')
            response = self.post(url, json=payload)
            return UploadResponse(**response.json())
        else:
            return
