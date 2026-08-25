fruits = ["apple", "banana", "cherry"]
print(fruits[0])
print(fruits[-1])
print(fruits[0:2])

fruits[0] = "avocado"
print(fruits)

fruits.append("date")
fruits.insert(1, "apricot")
print(fruits)

fruits.remove("banana")
print(fruits)

last = fruits.pop()
print(last, fruits)

for index, fruit in enumerate(fruits):
    print(index, fruit)

print("cherry" in fruits)
print(len(fruits))

numbers = [3, 1, 4, 1, 5]
new_list = sorted(numbers)
print(numbers)
print(new_list)
