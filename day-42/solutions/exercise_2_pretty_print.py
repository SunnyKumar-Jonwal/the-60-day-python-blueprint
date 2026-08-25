import json

data = {"name": "Ada", "skills": ["Python", "math"], "employed": True}

print(json.dumps(data, indent=2))
