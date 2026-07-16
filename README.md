# Italy Weather ETL Pipeline

This project collects weather data for Messina, Italy using the Open-Meteo API.  
It stores the raw API data, transforms it into a clean table, loads it into SQLite, and exports a daily weather summary CSV.

## Tools Used
- Python
- Pandas
- SQLite
- Open-Meteo API

## Project Structure
- `src/` : Python scripts
- `data/raw/` : raw JSON files
- `data/processed/` : cleaned CSV files
- `data/weather.db` : SQLite database
- `sql/` : SQL queries
- `output/` : final exported summary

## Pipeline Steps
1. Extract weather data from Open-Meteo API
2. Save raw JSON
3. Transform JSON into a structured CSV
4. Load cleaned data into SQLite
5. Create daily summary table
6. Export final summary CSV

## How to Run
```bash
python src/run_pipeline.py
python src/export_summary.py
```

## Output
The final output file is:
`output/daily_weather_summary.csv`

## Future Improvements
- Add more Italian cities
- Use PostgreSQL instead of SQLite
- Add scheduling
- Create charts and dashboard