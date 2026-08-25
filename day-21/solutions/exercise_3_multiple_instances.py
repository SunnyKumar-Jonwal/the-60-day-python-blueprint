class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def summary(self):
        return f"'{self.title}' by {self.author} ({self.pages} pages)"


book1 = Book("Dune", "Frank Herbert", 412)
book2 = Book("1984", "George Orwell", 328)
book3 = Book("Foundation", "Isaac Asimov", 255)

for book in (book1, book2, book3):
    print(book.summary())
