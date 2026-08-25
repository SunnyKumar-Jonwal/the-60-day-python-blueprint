from fastapi import FastAPI, HTTPException

app = FastAPI()

fake_books = {1: "Dune", 2: "1984"}

# TODO: add GET /books/{book_id} (book_id: int) that raises HTTPException
# (404, "Book not found") if book_id not in fake_books, else returns
# {"book_id": book_id, "title": fake_books[book_id]}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
