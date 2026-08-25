from app_4 import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_missing_field_returns_422():
    response = client.post("/products", json={"name": "Widget"})
    assert response.status_code == 422


def test_valid_product_returns_201():
    response = client.post("/products", json={"name": "Widget", "price": 9.99})
    assert response.status_code == 201
