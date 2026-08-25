class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def summary(self):
        return f"'{self.title}' by {self.author} ({self.pages} pages)"


# TODO: create three Book instances with different data
# TODO: print each one's summary()
