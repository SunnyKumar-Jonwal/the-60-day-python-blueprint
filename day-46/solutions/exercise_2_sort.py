import pandas as pd

sales = pd.read_csv("day-45/sales.csv")

sorted_sales = sales.sort_values("price", ascending=False)
print(sorted_sales.head())
