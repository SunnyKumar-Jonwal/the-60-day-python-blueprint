from app_4 import app
from fastapi.testclient import TestClient

client = TestClient(app)

# TODO: write test_missing_field_returns_422() that POSTs {"name": "Widget"}
# (missing required "price") to /products and asserts status_code == 422
# TODO: write test_valid_product_returns_201() that POSTs a full valid
# product ({"name": "Widget", "price": 9.99}) and asserts status_code == 201
