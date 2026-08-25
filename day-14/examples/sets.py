numbers = set([1, 2, 3, 2, 1])
print(numbers)

fruits = {"apple", "banana"}
fruits.add("cherry")
print(fruits)
fruits.remove("banana")
print(fruits)
fruits.discard("kiwi")
print(fruits)

print("cherry" in fruits)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)
print(a & b)
print(a - b)
print(a ^ b)
