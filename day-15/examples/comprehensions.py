squares = [n * n for n in range(5)]
print(squares)

evens = [n for n in range(10) if n % 2 == 0]
print(evens)

squares_by_number = {n: n * n for n in range(5)}
print(squares_by_number)

words = ["hi", "hello", "hey", "yo"]
unique_lengths = {len(word) for word in words}
print(unique_lengths)
