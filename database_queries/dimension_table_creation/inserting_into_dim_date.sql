INSERT INTO dim_date (full_date, year, month, day, week, quarter)
SELECT DISTINCT 
    date AS full_date,
    EXTRACT(YEAR FROM date) AS year,
    EXTRACT(MONTH FROM date) AS month,
    EXTRACT(DAY FROM date) AS day,
    EXTRACT(WEEK FROM date) AS week,
    EXTRACT(QUARTER FROM date) AS quarter
FROM carts;
