from app_2 import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_create_item():
    response = client.post("/items", json={"name": "Widget"})
    assert response.status_code == 201
    assert response.json()["name"] == "Widget"
