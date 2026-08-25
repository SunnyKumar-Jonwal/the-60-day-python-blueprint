from datetime import datetime, timedelta

start_date = datetime(2024, 1, 1)

later_date = start_date + timedelta(days=30)
print(later_date.strftime("%Y-%m-%d"))
