from backend.resume_upload.resume_upload_controller import UploadResponse, JobDescriptionPayload
from backend.models.enums import *
from tests.backend.base_client import TestApiBaseClient


def test_upload_resume_success():
    file = b"%PDF-1.4 Test Resume PDF File"
    test_client = TestApiBaseClient()
    resume_upload_response = test_client.upload_resume(file)
    expected_response = UploadResponse(message=ResumeUploadMessages.ResumeUploadSuccess, status=Status.Success)
    assert expected_response == resume_upload_response


def test_upload_resume_fail_too_large():
    file = b'Test Resume Text Wrong File'
    test_client = TestApiBaseClient()
    resume_upload_response = test_client.upload_resume(file, 'text/plain', 'test_resume.txt')
    expected_response = UploadResponse(message=ResumeUploadMessages.NotAPdf, status=Status.Error)
    assert expected_response == resume_upload_response


def test_upload_resume_fail_wrong_data_type():
    file = b"%PDF-1.4 Test Resume PDF File" + b"a" * (2 * 1024 * 1024)
    test_client = TestApiBaseClient()
    resume_upload_response = test_client.upload_resume(file)
    expected_response = UploadResponse(message=ResumeUploadMessages.TooLarge, status=Status.Error)
    assert expected_response == resume_upload_response


def test_upload_job_description_success():
    test_client = TestApiBaseClient()
    payload = JobDescriptionPayload(job_description="Job Job Job")
    job_description_upload_response = test_client.upload_job_description(payload)
    expected_response = UploadResponse(message=ResumeUploadMessages.JobDescriptionUploadSuccess, status=Status.Success)
    assert expected_response == job_description_upload_response


def test_upload_job_description_fail():
    payload = JobDescriptionPayload(job_description="a" * 5005)
    test_client = TestApiBaseClient()
    job_description_upload_response = test_client.upload_job_description(payload)
    expected_response = UploadResponse(message=ResumeUploadMessages.JobDescriptionUploadFailure, status=Status.Error)
    assert expected_response == job_description_upload_response
