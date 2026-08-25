person = {"name": "Ada", "age": 30}
print(person["name"])
print(person.get("email"))
print(person.get("email", "unknown"))

person["email"] = "ada@example.com"
person["age"] = 31
print(person)

del person["email"]
print(person)

print("name" in person)
print("Ada" in person)

for key, value in person.items():
    print(key, value)
