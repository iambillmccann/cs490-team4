from backend.models.storage import TempStorage


def test_temp_storage():
    resume_text = "Resume Text"
    job_description = "Job Description"
    storage = TempStorage()
    storage_uid = storage.create(resume_text, job_description)
    assert storage.read(storage_uid) is not None

    data = storage.read(storage_uid)
    assert data["resume_text"] == resume_text
    assert data["job_description"] == job_description

    clear = storage.delete(storage_uid)
    assert clear is True
    assert storage.read(storage_uid) is None

    clear = storage.delete(storage_uid)
    assert clear is False
