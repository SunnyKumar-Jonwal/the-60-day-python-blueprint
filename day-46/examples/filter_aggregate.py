import pandas as pd

sales = pd.read_csv("day-45/sales.csv")

electronics = sales[sales["category"] == "Electronics"]
print(electronics)

big_orders = sales[sales["quantity"] > 10]
print(big_orders)

both = sales[(sales["category"] == "Electronics") & (sales["quantity"] > 5)]
print(both)

sorted_desc = sales.sort_values("quantity", ascending=False)
print(sorted_desc.head())

sales["total"] = sales["quantity"] * sales["price"]
print(sales[["product", "quantity", "price", "total"]].head())

totals_by_category = sales.groupby("category")["quantity"].sum()
print(totals_by_category)

print(sales.groupby("category")["price"].mean())
print(sales.groupby("category").size())
print(sales.groupby("category")["quantity"].agg(["sum", "mean", "max"]))
