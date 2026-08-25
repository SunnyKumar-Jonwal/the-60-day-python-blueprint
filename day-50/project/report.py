from analysis import (
    average_temperature_by_city,
    days_above_threshold,
    hottest_day,
    load_weather,
    total_precipitation_by_city,
)

WEATHER_FILE = "day-50/project/weather.csv"


def main():
    df = load_weather(WEATHER_FILE)

    print("=== Average temperature by city (C) ===")
    print(average_temperature_by_city(df).round(1))

    print("\n=== Hottest day ===")
    hottest = hottest_day(df)
    print(f"{hottest['city']} on {hottest['date']}: {hottest['temperature_c']}C")

    print("\n=== Total precipitation by city (mm) ===")
    print(total_precipitation_by_city(df).round(1))

    print("\n=== Days above 30C ===")
    for city in df["city"].unique():
        print(f"{city}: {days_above_threshold(df, city, 30)}")


if __name__ == "__main__":
    main()
