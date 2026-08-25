import re

sentence = "Please mail the package to zip code 90210 by Friday."

match = re.search(r"\d{5}", sentence)
print(match.group())
