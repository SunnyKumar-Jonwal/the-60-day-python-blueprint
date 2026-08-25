import pandas as pd

sales = pd.read_csv("day-45/sales.csv")

print(sales[["product", "quantity"]])
