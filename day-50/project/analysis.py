import pandas as pd


def load_weather(path):
    return pd.read_csv(path)


def average_temperature_by_city(df):
    return df.groupby("city")["temperature_c"].mean()


def hottest_day(df):
    return df.loc[df["temperature_c"].idxmax()]


def total_precipitation_by_city(df):
    return df.groupby("city")["precipitation_mm"].sum()


def days_above_threshold(df, city, threshold):
    city_df = df[df["city"] == city]
    return int((city_df["temperature_c"] > threshold).sum())
