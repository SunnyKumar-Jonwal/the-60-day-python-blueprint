from datetime import datetime

text = "2024-12-25"

parsed = datetime.strptime(text, "%Y-%m-%d")
print(parsed.year)
print(parsed.month)
print(parsed.day)
