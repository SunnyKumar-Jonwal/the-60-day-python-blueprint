from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200


def test_list_books_includes_seeded_data():
    response = client.get("/books")
    assert response.status_code == 200
    books = response.json()
    assert len(books) == 15
    assert any(book["title"] == "Dune" for book in books)


def test_read_existing_book():
    response = client.get("/books/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Dune"


def test_read_missing_book_returns_404():
    response = client.get("/books/99999")
    assert response.status_code == 404


def test_create_and_delete_book():
    create_response = client.post(
        "/books",
        json={
            "title": "Test Book",
            "author": "Test Author",
            "genre": "Test",
            "year": 2024,
            "copies_available": 1,
        },
    )
    assert create_response.status_code == 201
    book_id = create_response.json()["id"]

    read_response = client.get(f"/books/{book_id}")
    assert read_response.status_code == 200

    delete_response = client.delete(f"/books/{book_id}")
    assert delete_response.status_code == 204

    final_read = client.get(f"/books/{book_id}")
    assert final_read.status_code == 404


def test_update_book():
    response = client.put(
        "/books/2",
        json={
            "title": "Foundation",
            "author": "Isaac Asimov",
            "genre": "Sci-Fi",
            "year": 1951,
            "copies_available": 10,
        },
    )
    assert response.status_code == 200
    assert response.json()["copies_available"] == 10


def test_checkout_reduces_available_copies():
    before = client.get("/books/1").json()["copies_available"]
    response = client.post("/books/1/checkout")
    assert response.status_code == 200
    assert response.json()["copies_available"] == before - 1


def test_checkout_with_no_copies_returns_409():
    # "The Name of the Wind" is seeded with 0 copies available (see books.csv)
    response = client.post("/books/6/checkout")
    assert response.status_code == 409


def test_search_finds_matching_books():
    response = client.get("/books/search", params={"query": "Frank Herbert"})
    assert response.status_code == 200
    results = response.json()
    assert len(results) == 1
    assert results[0]["title"] == "Dune"


def test_stats_reflects_seeded_data():
    response = client.get("/books/stats")
    assert response.status_code == 200
    stats = response.json()
    assert stats["total_books"] == 15
    assert "Sci-Fi" in stats["books_by_genre"]
