class LibraryError(Exception):
    """Base class for every domain error this library API can raise."""


class BookNotFoundError(LibraryError):
    pass


class NoCopiesAvailableError(LibraryError):
    pass


class Book:
    def __init__(self, id, title, author, genre, year, copies_available):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        self.copies_available = copies_available

    def checkout(self):
        if self.copies_available <= 0:
            raise NoCopiesAvailableError(f"No copies of '{self.title}' are available")
        self.copies_available -= 1

    def __str__(self):
        return f"{self.title} by {self.author} ({self.copies_available} available)"

    def __repr__(self):
        return f"Book(id={self.id}, title={self.title!r}, copies_available={self.copies_available})"

    def __eq__(self, other):
        return isinstance(other, Book) and self.id == other.id
