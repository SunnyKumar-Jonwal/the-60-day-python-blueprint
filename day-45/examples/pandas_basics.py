import pandas as pd

sales = pd.read_csv("day-45/sales.csv")

print(sales.head())
print(sales.head(3))
print(sales.shape)
print(sales.columns)
sales.info()
print(sales.describe())

print(sales["product"])
print(sales[["product", "price"]])

print(sales.iloc[0])
print(sales.iloc[0:3])
print(sales.loc[0])
