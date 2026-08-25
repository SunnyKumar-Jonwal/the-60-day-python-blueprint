class Book:
    def describe(self):
        return "A paperback novel"


class Movie:
    def describe(self):
        return "A two-hour film"


items = [Book(), Movie()]
for item in items:
    print(item.describe())
