import os
import json
import logging
import pandas as pd
from glob import glob
from config import CITY_NAME

logger = logging.getLogger(__name__)


def get_latest_raw_file():
    files = glob("data/raw/*.json")
    if not files:
        raise FileNotFoundError("No raw JSON files found in data/raw/")
    return max(files, key=os.path.getctime)


def transform_weather():
    try:
        logger.info("Starting weather data transformation")

        raw_file = get_latest_raw_file()
        logger.info(f"Latest raw file found: {raw_file}")

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

        if df.empty:
            raise ValueError("Transformed DataFrame is empty")

        required_columns = [
            "timestamp",
            "temperature_2m",
            "relative_humidity_2m",
            "precipitation",
            "wind_speed_10m",
            "weather_code"
        ]

        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}")

        df["city"] = CITY_NAME
        df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

        if df["timestamp"].isna().any():
            raise ValueError("Some timestamp values could not be converted to datetime")

        duplicate_count = df.duplicated(subset=["timestamp"]).sum()
        if duplicate_count > 0:
            raise ValueError(f"Found {duplicate_count} duplicate timestamp rows")

        logger.info(f"Weather data transformed successfully with {len(df)} rows")
        logger.info("Validation passed: required columns, timestamps, and duplicates check")

        os.makedirs("data/processed", exist_ok=True)
        output_file = f"data/processed/{CITY_NAME.lower()}_hourly_weather.csv"
        df.to_csv(output_file, index=False)

        logger.info(f"Processed weather data saved to: {output_file}")

    except FileNotFoundError as e:
        logger.exception(f"File error in transform_weather: {e}")
        raise

    except KeyError as e:
        logger.exception(f"Missing expected JSON key in transform_weather: {e}")
        raise

    except ValueError as e:
        logger.exception(f"Validation/value error in transform_weather: {e}")
        raise

    except Exception as e:
        logger.exception(f"Unexpected error in transform_weather: {e}")
        raise


if __name__ == "__main__":
    transform_weather()