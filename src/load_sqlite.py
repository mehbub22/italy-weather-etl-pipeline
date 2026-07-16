import os
import sqlite3
import pandas as pd

DB_PATH = "data/weather.db"
CSV_PATH = "data/processed/messina_hourly_weather.csv"

def load_to_sqlite():
    if not os.path.exists(CSV_PATH):
        raise FileNotFoundError(f"CSV file not found: {CSV_PATH}")

    df = pd.read_csv(CSV_PATH)

    conn = sqlite3.connect(DB_PATH)

    df.to_sql("stg_hourly_weather", conn, if_exists="replace", index=False)

    conn.execute("DROP TABLE IF EXISTS mart_daily_weather_summary")

    conn.execute("""
        CREATE TABLE mart_daily_weather_summary AS
        SELECT
            city,
            date(timestamp) AS date,
            ROUND(AVG(temperature_2m), 2) AS avg_temp,
            ROUND(MIN(temperature_2m), 2) AS min_temp,
            ROUND(MAX(temperature_2m), 2) AS max_temp,
            ROUND(SUM(precipitation), 2) AS total_precipitation,
            ROUND(MAX(wind_speed_10m), 2) AS max_wind_speed
        FROM stg_hourly_weather
        GROUP BY city, date(timestamp)
    """)

    result = pd.read_sql_query("SELECT * FROM mart_daily_weather_summary", conn)
    print(result.head())

    conn.close()
    print(f"Data loaded into SQLite database: {DB_PATH}")

if __name__ == "__main__":
    load_to_sqlite()