class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


book = Book("Dune", "Frank Herbert", 412)
print(book.title)
print(book.author)
print(book.pages)
