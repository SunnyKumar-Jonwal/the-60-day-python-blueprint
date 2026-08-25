import pandas as pd

sales = pd.read_csv("day-45/sales.csv")

accessories = sales[sales["category"] == "Accessories"]
print(accessories)
