from fastapi.testclient import TestClient
from starlette import status
from app.main import app #importing the app from the main.py file, where we have the FastAPI instance

client=TestClient(app)

def test_health_live_returns_200():
    #first step is to get the response from the endpoint
    response=client.get("/health/live")

    #Second step is to check the response status code and the response body
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "alive"}
