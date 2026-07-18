from logger import setup_logger
from extract_weather import fetch_weather
from transform_weather import transform_weather
from load_sqlite import load_to_sqlite

logger = setup_logger()


def run_pipeline():
    try:
        logger.info("Pipeline started")

        logger.info("Step 1: Extracting weather data...")
        fetch_weather()

        logger.info("Step 2: Transforming weather data...")
        transform_weather()

        logger.info("Step 3: Loading data into SQLite...")
        load_to_sqlite()

        logger.info("Pipeline completed successfully.")

    except Exception as e:
        logger.exception(f"Pipeline failed: {e}")


if __name__ == "__main__":
    run_pipeline()