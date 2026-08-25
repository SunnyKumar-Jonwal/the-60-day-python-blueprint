import pandas as pd

sales = pd.read_csv("day-45/sales.csv")

totals = sales.groupby("category")["quantity"].sum()
print(totals.sort_values(ascending=False))
