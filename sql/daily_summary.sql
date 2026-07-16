SELECT
    city,
    date(timestamp) AS date,
    ROUND(AVG(temperature_2m), 2) AS avg_temp,
    ROUND(MIN(temperature_2m), 2) AS min_temp,
    ROUND(MAX(temperature_2m), 2) AS max_temp,
    ROUND(SUM(precipitation), 2) AS total_precipitation,
    ROUND(MAX(wind_speed_10m), 2) AS max_wind_speed
FROM stg_hourly_weather
GROUP BY city, date(timestamp);