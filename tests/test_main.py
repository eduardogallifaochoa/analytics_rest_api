from fastapi.testclient import TestClient
from app.main import app

# Create a TestClient instance to simulate HTTP requests to the FastAPI app
client = TestClient(app)

def test_read_root():
    """
    Test the /hello endpoint.
    Verifies that the response status is 200 and the JSON message is correct.
    """
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_predict_with_name():
    """
    Test the /predict endpoint with a query parameter.
    Verifies that the response includes the provided name.
    """
    response = client.get("/predict?name=Eddie")
    assert response.status_code == 200
    assert "Eddie" in response.json()["prediction"]

def test_predict_default():
    """
    Test the /predict endpoint without a query parameter.
    Verifies that the default value 'User' is used in the response.
    """
    response = client.get("/predict")
    assert response.status_code == 200
    assert "User" in response.json()["prediction"]
