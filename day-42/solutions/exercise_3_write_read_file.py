import json

data = {"city": "London", "population": 8982000}

with open("day-42/exercises_output.json", "w") as file:
    json.dump(data, file)

with open("day-42/exercises_output.json") as file:
    loaded = json.load(file)

print(loaded)
