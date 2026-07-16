# Italy Weather ETL Pipeline

This project is a beginner-friendly data engineering project.  
It collects weather data for Messina, Italy from the Open-Meteo API, saves the raw data, transforms it into a clean table, loads it into SQLite, and exports a daily summary CSV file.

## Project Goal

The goal of this project is to practice the basic ETL process:

- Extract weather data from an API
- Transform the raw JSON data into a structured table
- Load the cleaned data into a SQLite database
- Export a final summary file for analysis

This project is designed as a simple portfolio project for learning data engineering concepts using Python and SQL.

## Tools Used

- Python
- Pandas
- SQLite
- Open-Meteo API
- Git and GitHub
- VS Code

## Project Structure

```text
italy-weather-etl-pipeline/
│
├── .gitignore
├── README.md
├── requirements.txt
├── data/
│   ├── raw/
│   ├── processed/
│   └── weather.db
├── output/
│   └── daily_weather_summary.csv
├── sql/
│   ├── daily_summary.sql
│   ├── extreme_days.sql
│   └── windy_days.sql
├── notebooks/
└── src/
    ├── config.py
    ├── extract_weather.py
    ├── transform_weather.py
    ├── load_sqlite.py
    ├── run_pipeline.py
    └── export_summary.py
```

## How the Pipeline Works

The pipeline works in 5 main steps:

1. Extract weather data from the Open-Meteo API
2. Save the raw response as a JSON file
3. Transform the data into a clean CSV file
4. Load the cleaned data into SQLite and create a daily summary table
5. Export the final summary as a CSV file

## Data Source

This project uses the Open-Meteo API to collect hourly weather data for Messina, Italy.

Main variables used:
- temperature_2m
- relative_humidity_2m
- precipitation
- wind_speed_10m
- weather_code

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/mehbub22/italy-weather-etl-pipeline.git
cd italy-weather-etl-pipeline
```

### 2. Create and activate a virtual environment

On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Run the full pipeline

```bash
python src/run_pipeline.py
```

### 5. Export the final summary file

```bash
python src/export_summary.py
```

## Output

The main output files are:

- `data/processed/messina_hourly_weather.csv` → cleaned hourly weather data
- `data/weather.db` → SQLite database
- `output/daily_weather_summary.csv` → final exported daily summary

## Example SQL Files

This project also includes some SQL queries:

- `daily_summary.sql` → creates daily aggregated weather data
- `extreme_days.sql` → shows the hottest days
- `windy_days.sql` → shows the windiest days

## What I Learned

Through this project, I practiced:

- Working with APIs
- Handling JSON data in Python
- Transforming data using Pandas
- Loading data into SQLite
- Writing SQL queries
- Using Git and GitHub for project version control

## Future Improvements

Possible future improvements for this project:

- Add more Italian cities such as Palermo and Rome
- Replace SQLite with PostgreSQL
- Add data visualization charts
- Automate the pipeline with scheduling
- Build a dashboard for weather insights
