import numpy as np

numbers = np.array([1, 2, 3, 4, 5])
print(numbers)
print(type(numbers))

matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)

print(numbers * 2)
print(numbers + 10)
print(numbers**2)

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print(a + b)

print(numbers[0])
print(numbers[-1])
print(numbers[1:3])

print(matrix.shape)
print(matrix[0, 1])

scores = np.array([4, 8, 15, 16, 23, 42])
print(scores.sum())
print(scores.mean())
print(scores.min())
print(scores.max())
