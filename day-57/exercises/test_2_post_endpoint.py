from app_2 import app
from fastapi.testclient import TestClient

client = TestClient(app)

# TODO: write test_create_item() that POSTs {"name": "Widget"} to /items,
# asserts status_code == 201, and asserts response.json()["name"] == "Widget"
