import re

text = "My phone number is 555-1234"
match = re.search(r"\d{3}-\d{4}", text)
print(match.group())

print(re.match(r"\d+", "abc123"))
print(re.search(r"\d+", "abc123").group())

multi_text = "Call 555-1234 or 555-5678"
numbers = re.findall(r"\d{3}-\d{4}", multi_text)
print(numbers)

masked = re.sub(r"\d{3}-\d{4}", "[REDACTED]", "Contact: 555-1234")
print(masked)

group_match = re.search(r"(\d{3})-(\d{4})", "555-1234")
print(group_match.group())
print(group_match.group(1))
print(group_match.group(2))
