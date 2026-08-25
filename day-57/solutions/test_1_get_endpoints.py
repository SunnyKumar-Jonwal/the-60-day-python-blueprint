from app_1 import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Items API"}


def test_read_existing_item():
    response = client.get("/items/1")
    assert response.status_code == 200


def test_read_missing_item():
    response = client.get("/items/999")
    assert response.status_code == 404
