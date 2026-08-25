from fastapi import FastAPI, HTTPException

app = FastAPI()

fake_books = {1: "Dune", 2: "1984"}


@app.get("/books/{book_id}")
def read_book(book_id: int):
    if book_id not in fake_books:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"book_id": book_id, "title": fake_books[book_id]}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
