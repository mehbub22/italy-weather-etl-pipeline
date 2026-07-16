import os
import sqlite3
import pandas as pd

DB_PATH = "data/weather.db"
OUTPUT_PATH = "output/daily_weather_summary.csv"

def export_summary():
    conn = sqlite3.connect(DB_PATH)

    query = "SELECT * FROM mart_daily_weather_summary ORDER BY date"
    df = pd.read_sql_query(query, conn)

    os.makedirs("output", exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)

    conn.close()
    print(f"Summary exported to: {OUTPUT_PATH}")

if __name__ == "__main__":
    export_summary()