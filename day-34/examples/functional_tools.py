from functools import reduce

print((lambda n: n * n)(5))

numbers = [1, 2, 3, 4]
squared = list(map(lambda n: n * n, numbers))
print(squared)

evens = list(filter(lambda n: n % 2 == 0, numbers))
print(evens)

total = reduce(lambda acc, n: acc + n, numbers)
print(total)

words = ["hello", "world"]
print(list(map(str.upper, words)))
