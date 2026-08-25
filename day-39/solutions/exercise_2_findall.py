import re

text = "Contact ada@example.com or grace@example.org for details."

emails = re.findall(r"\w+@\w+\.\w+", text)
print(emails)
