import os
import json
import pandas as pd
from glob import glob
from config import CITY_NAME

def get_latest_raw_file():
    files = glob("data/raw/*.json")
    if not files:
        raise FileNotFoundError("No raw JSON files found in data/raw/")
    return max(files, key=os.path.getctime)

def transform_weather():
    raw_file = get_latest_raw_file()

    with open(raw_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    hourly = data["hourly"]

    df = pd.DataFrame({
        "timestamp": hourly["time"],
        "temperature_2m": hourly["temperature_2m"],
        "relative_humidity_2m": hourly["relative_humidity_2m"],
        "precipitation": hourly["precipitation"],
        "wind_speed_10m": hourly["wind_speed_10m"],
        "weather_code": hourly["weather_code"]
    })

    df["city"] = CITY_NAME
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    os.makedirs("data/processed", exist_ok=True)
    output_file = f"data/processed/{CITY_NAME.lower()}_hourly_weather.csv"
    df.to_csv(output_file, index=False)

    print(f"Processed weather data saved to: {output_file}")
    print(df.head())

if __name__ == "__main__":
    transform_weather()