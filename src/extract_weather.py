import os
import json
import logging
from datetime import datetime
import requests
from config import CITY_NAME, LATITUDE, LONGITUDE, TIMEZONE, HOURLY_VARS

logger = logging.getLogger(__name__)


def fetch_weather():
    try:
        logger.info("Starting weather data extraction")

        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": LATITUDE,
            "longitude": LONGITUDE,
            "hourly": ",".join(HOURLY_VARS),
            "timezone": TIMEZONE
        }

        logger.info(f"Sending request to Open-Meteo API for city: {CITY_NAME}")
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()

        data = response.json()
        logger.info("Weather data received successfully from API")

        os.makedirs("data/raw", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = f"data/raw/{CITY_NAME.lower()}_weather_raw_{timestamp}.json"

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        logger.info(f"Raw weather data saved to: {file_path}")

    except requests.exceptions.Timeout:
        logger.exception("Request timed out while fetching weather data")
        raise

    except requests.exceptions.RequestException as e:
        logger.exception(f"Request error while fetching weather data: {e}")
        raise

    except Exception as e:
        logger.exception(f"Unexpected error in fetch_weather: {e}")
        raise


if __name__ == "__main__":
    fetch_weather()