class EvenNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    # TODO: add __next__ that returns the next even number (starting at 2),
    # raising StopIteration once it would exceed self.limit


# TODO: loop over EvenNumbers(10) and print each value (should print 2, 4, 6, 8, 10)
