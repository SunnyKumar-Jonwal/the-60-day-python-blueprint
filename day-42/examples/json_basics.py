import json

person = {"name": "Ada", "age": 30, "active": True}
json_text = json.dumps(person)
print(json_text)
print(type(json_text))

print(json.dumps(person, indent=2))

loaded = json.loads(json_text)
print(loaded)
print(type(loaded))
print(loaded["name"])

with open("day-42/examples_output.json", "w") as file:
    json.dump(person, file, indent=2)

with open("day-42/examples_output.json") as file:
    reloaded = json.load(file)
print(reloaded)

data = {
    "user": {"name": "Ada", "roles": ["admin", "editor"]},
    "active": True,
}
print(data["user"]["name"])
print(data["user"]["roles"][0])
