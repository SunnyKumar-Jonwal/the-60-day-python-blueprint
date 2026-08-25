from app_3 import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_full_crud_flow():
    create_response = client.post("/tasks", json={"title": "Buy milk"})
    assert create_response.status_code == 201
    task_id = create_response.json()["id"]

    read_response = client.get(f"/tasks/{task_id}")
    assert read_response.status_code == 200
    assert read_response.json()["title"] == "Buy milk"

    update_response = client.put(f"/tasks/{task_id}", json={"title": "Buy oat milk"})
    assert update_response.status_code == 200
    assert update_response.json()["title"] == "Buy oat milk"

    delete_response = client.delete(f"/tasks/{task_id}")
    assert delete_response.status_code == 204

    final_read = client.get(f"/tasks/{task_id}")
    assert final_read.status_code == 404
