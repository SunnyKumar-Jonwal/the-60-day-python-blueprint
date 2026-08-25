def even_numbers():
    current = 0
    while True:
        current += 2
        yield current


gen = even_numbers()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
