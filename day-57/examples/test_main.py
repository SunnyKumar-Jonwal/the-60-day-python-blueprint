from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}


def test_create_item():
    response = client.post("/items", json={"name": "Widget"})
    assert response.status_code == 201
    body = response.json()
    assert body["name"] == "Widget"
    assert "id" in body


def test_read_existing_item():
    created = client.post("/items", json={"name": "Gadget"}).json()
    response = client.get(f"/items/{created['id']}")
    assert response.status_code == 200
    assert response.json()["name"] == "Gadget"


def test_read_missing_item_returns_404():
    response = client.get("/items/99999")
    assert response.status_code == 404
