def make_accumulator():
    total = 0

    def add(n):
        nonlocal total
        total += n
        return total

    return add


acc = make_accumulator()
print(acc(10))
print(acc(5))
print(acc(3))
