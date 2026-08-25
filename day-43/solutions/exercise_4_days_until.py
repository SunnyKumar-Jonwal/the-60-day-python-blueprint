from datetime import datetime

target_date = datetime(2030, 1, 1)

difference = target_date - datetime.now()
print(difference.days)
