import json

original = {"title": "Dune", "year": 1965}

json_text = json.dumps(original)
round_tripped = json.loads(json_text)
print(round_tripped == original)
