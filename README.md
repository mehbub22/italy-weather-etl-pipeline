# Italy Weather ETL Pipeline

A simple end-to-end ETL pipeline built in Python that fetches hourly weather data for Messina from the Open-Meteo API, transforms and validates it with pandas, and loads the cleaned data into SQLite for analysis. This project was created as a beginner-friendly data engineering portfolio project to demonstrate API ingestion, transformation, validation, logging, and database loading. [Open-Meteo](https://open-meteo.com/) provides the weather data used in this pipeline.

## Project Overview

The goal of this project is to build a small but structured ETL pipeline that simulates a real data engineering workflow.

The pipeline does the following:
- Extracts hourly weather data from the Open-Meteo API
- Saves raw JSON files in the `data/raw/` folder
- Transforms the raw JSON into a structured pandas DataFrame
- Validates the transformed data
- Saves the processed data as CSV
- Loads the processed data into a SQLite database
- Creates a summary mart table with daily weather metrics
- Logs pipeline activity into a log file for debugging and monitoring

## Tech Stack

- Python
- pandas
- requests
- SQLite
- logging
- VS Code

## Project Structure

```bash
italy-weather-etl-pipeline/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── weather.db
│
├── logs/
│   └── pipeline.log
│
├── sql/
│   ├── daily_summary.sql
│   ├── extreme_days.sql
│   └── windy_days.sql
│
├── src/
│   ├── config.py
│   ├── logger.py
│   ├── extract_weather.py
│   ├── transform_weather.py
│   ├── load_sqlite.py
│   ├── export_summary.py
│   └── run_pipeline.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Pipeline Flow

1. `extract_weather.py` fetches hourly weather data from the Open-Meteo API and saves it as a timestamped raw JSON file.
2. `transform_weather.py` reads the most recent raw JSON file and converts it into a structured CSV file.
3. Validation checks are applied during transformation:
   - DataFrame is not empty
   - Required columns exist
   - Timestamps are valid
   - No duplicate timestamps exist
4. `load_sqlite.py` loads the processed CSV into SQLite.
5. A summary table called `mart_daily_weather_summary` is created for daily analytics.
6. `run_pipeline.py` orchestrates the full ETL pipeline and logs each step.

## Validation and Logging

This project includes basic data engineering improvements:
- File and terminal logging using Python's `logging` module
- Validation checks during transformation
- Error handling for extraction, transformation, and loading
- Clean ETL structure with separated modules

The log file is stored at:

```bash
logs/pipeline.log
```

## Example Output

The final SQLite database contains:
- `stg_hourly_weather` for hourly processed weather data
- `mart_daily_weather_summary` for daily summary metrics

Example daily summary columns:
- `city`
- `date`
- `avg_temp`
- `min_temp`
- `max_temp`
- `total_precipitation`
- `max_wind_speed`

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/mehbub22/italy-weather-etl-pipeline.git
cd italy-weather-etl-pipeline
```

### 2. Create and activate a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the pipeline

```bash
python src/run_pipeline.py
```

## Sample Output Files

After running the pipeline, you should see:
- raw JSON files in `data/raw/`
- processed CSV files in `data/processed/`
- SQLite database in `data/weather.db`
- logs in `logs/pipeline.log`

## What I Learned

Through this project, I practiced:
- working with an external API
- building a multi-step ETL pipeline
- transforming JSON data into tabular format
- validating data before loading
- loading data into SQLite
- using logging for debugging and monitoring
- structuring a Python project for GitHub

## Future Improvements

Possible next improvements:
- support multiple Italian cities
- add retry logic for failed API requests
- make the pipeline safe for repeated runs without duplicates
- move from SQLite to PostgreSQL
- schedule the pipeline with cron or Airflow
- create a dashboard for visualizing daily weather summaries

## Data Source

Weather data is provided by the [Open-Meteo API](https://open-meteo.com/).

## Author

**Mehbub22**

Data Analytics student interested in Data Engineering, Machine Learning, and analytics projects.