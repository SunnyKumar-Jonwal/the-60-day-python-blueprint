from app_1 import app
from fastapi.testclient import TestClient

client = TestClient(app)

# TODO: write test_read_root() asserting status 200 and json() == {"message": "Items API"}
# TODO: write test_read_existing_item() asserting status 200 for GET /items/1
# TODO: write test_read_missing_item() asserting status 404 for GET /items/999
