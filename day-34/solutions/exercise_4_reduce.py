from functools import reduce

numbers = [1, 2, 3, 4, 5]

product = reduce(lambda acc, n: acc * n, numbers)
print(product)
