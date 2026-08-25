from app_3 import app
from fastapi.testclient import TestClient

client = TestClient(app)

# TODO: write test_full_crud_flow() that, in order:
# 1. POSTs {"title": "Buy milk"} to /tasks, asserts 201, saves the returned id
# 2. GETs /tasks/{id}, asserts 200 and the title matches
# 3. PUTs {"title": "Buy oat milk"} to /tasks/{id}, asserts 200 and the new title
# 4. DELETEs /tasks/{id}, asserts 204
# 5. GETs /tasks/{id} again, asserts 404
