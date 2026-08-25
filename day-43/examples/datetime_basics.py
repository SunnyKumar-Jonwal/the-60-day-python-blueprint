from datetime import datetime, timedelta

now = datetime.now()
print(now.strftime("%Y-%m-%d"))
print(now.strftime("%B %d, %Y"))

birthday = datetime(2024, 8, 25)
print(birthday.year, birthday.month, birthday.day)

text = "2024-08-25"
parsed = datetime.strptime(text, "%Y-%m-%d")
print(parsed)
print(parsed.year)

tomorrow = now + timedelta(days=1)
difference = tomorrow - now
print(difference.days)

deadline = datetime(2030, 12, 31)
print(now < deadline)
