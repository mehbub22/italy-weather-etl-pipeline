from extract_weather import fetch_weather
from transform_weather import transform_weather
from load_sqlite import load_to_sqlite

def run_pipeline():
    print("Step 1: Extracting weather data...")
    fetch_weather()

    print("Step 2: Transforming weather data...")
    transform_weather()

    print("Step 3: Loading data into SQLite...")
    load_to_sqlite()

    print("Pipeline completed successfully.")

if __name__ == "__main__":
    run_pipeline()