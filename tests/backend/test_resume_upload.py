from backend.app import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_upload_resume():
    response = client.post('/resume_upload', json={"Resume": "", "DataType": ""})
    assert response.status_code == 200
