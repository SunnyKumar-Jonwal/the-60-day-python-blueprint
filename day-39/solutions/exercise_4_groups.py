import re

date = "2024-08-25"

match = re.search(r"(\d{4})-(\d{2})-(\d{2})", date)
print(match.group(1))
print(match.group(2))
print(match.group(3))
