CREATE TABLE dim_date (
    date_id SERIAL PRIMARY KEY,  
    full_date DATE UNIQUE,       
    year INT,
    month INT,
    day INT,
    week INT,
    quarter INT
);
