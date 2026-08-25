class EvenNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 2
        if self.current > self.limit:
            raise StopIteration
        return self.current


for number in EvenNumbers(10):
    print(number)
