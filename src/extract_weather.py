import os
import json
from datetime import datetime
import requests
from config import CITY_NAME, LATITUDE, LONGITUDE, TIMEZONE, HOURLY_VARS

def fetch_weather():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "hourly": ",".join(HOURLY_VARS),
        "timezone": TIMEZONE
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    data = response.json()

    os.makedirs("data/raw", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"data/raw/{CITY_NAME.lower()}_weather_raw_{timestamp}.json"

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"Raw weather data saved to: {file_path}")

if __name__ == "__main__":
    fetch_weather()