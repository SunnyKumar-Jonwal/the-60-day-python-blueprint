import pandas as pd

sales = pd.read_csv("day-45/sales.csv")

sales["total"] = sales["quantity"] * sales["price"]
print(sales.sort_values("total", ascending=False))
