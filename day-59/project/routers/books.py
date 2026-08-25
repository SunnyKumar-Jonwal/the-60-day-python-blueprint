from fastapi import APIRouter, HTTPException, Response
from models import Book, BookNotFoundError, NoCopiesAvailableError
from pydantic import BaseModel
from repository import BookRepository

router = APIRouter(prefix="/books", tags=["books"])
repository = BookRepository()


class BookIn(BaseModel):
    title: str
    author: str
    genre: str
    year: int
    copies_available: int


def book_to_dict(book):
    return {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "genre": book.genre,
        "year": book.year,
        "copies_available": book.copies_available,
    }


@router.get("")
def list_books():
    return [book_to_dict(book) for book in repository.list_all()]


@router.get("/stats")
def stats():
    return repository.get_stats()


@router.get("/search")
def search(query: str):
    return [book_to_dict(book) for book in repository.search(query)]


@router.get("/{book_id}")
def read_book(book_id: int):
    try:
        return book_to_dict(repository.get(book_id))
    except BookNotFoundError as error:
        raise HTTPException(status_code=404, detail=str(error)) from error


@router.post("", status_code=201)
def create_book(book: BookIn):
    new_book = Book(None, book.title, book.author, book.genre, book.year, book.copies_available)
    created = repository.add(new_book)
    return book_to_dict(created)


@router.put("/{book_id}")
def update_book(book_id: int, book: BookIn):
    try:
        updated = repository.update(
            book_id, book.title, book.author, book.genre, book.year, book.copies_available
        )
        return book_to_dict(updated)
    except BookNotFoundError as error:
        raise HTTPException(status_code=404, detail=str(error)) from error


@router.delete("/{book_id}", status_code=204)
def delete_book(book_id: int):
    try:
        repository.delete(book_id)
    except BookNotFoundError as error:
        raise HTTPException(status_code=404, detail=str(error)) from error
    return Response(status_code=204)


@router.post("/{book_id}/checkout")
def checkout_book(book_id: int):
    try:
        book = repository.checkout(book_id)
        return book_to_dict(book)
    except BookNotFoundError as error:
        raise HTTPException(status_code=404, detail=str(error)) from error
    except NoCopiesAvailableError as error:
        raise HTTPException(status_code=409, detail=str(error)) from error
