from backend.main import app
from fastapi.testclient import TestClient


def test_healthcheck() -> None:
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
