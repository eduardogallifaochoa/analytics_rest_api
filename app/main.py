from fastapi import FastAPI
from typing import Dict

# Create the FastAPI instance
app = FastAPI()

@app.get("/hello")
def read_root() -> Dict[str, str]:
    """
    Simple GET endpoint that returns a greeting message.
    Use this to verify the API is working.
    """
    return {"message": "Hello, World!"}

@app.get("/predict")
def predict(name: str = "User") -> Dict[str, str]:
    """
    Simulates a prediction endpoint.
    Accepts a query parameter 'name' and returns a custom message.
    Example: /predict?name=Eddie
    """
    return {"prediction": f"Hello {name}, your data looks good for analysis!"}
