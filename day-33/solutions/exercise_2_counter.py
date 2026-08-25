def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


counter_a = make_counter()
counter_b = make_counter()

print(counter_a())
print(counter_a())
print(counter_b())
