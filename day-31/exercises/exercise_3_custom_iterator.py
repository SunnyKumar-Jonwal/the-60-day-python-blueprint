class CountDown:
    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        return self

    # TODO: add __next__ that returns self.current, decrementing it each call,
    # and raises StopIteration once self.current is below 1


# TODO: loop over CountDown(3) and print each value (should print 3, 2, 1)
