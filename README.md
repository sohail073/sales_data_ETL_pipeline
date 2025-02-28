# sales_data_ETL_pipeline

This project is designed to extract, transform, and load (ETL) data from various APIs into a PostgreSQL database. The data includes products, carts, and users information.

## Project Structure

```
Airflow project/
│
├── src/
│   ├── main.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── config.py
│
├── database/
│   ├── creating_products_table.sql
│   ├── creating_carts_table.sql
│   └── creating_users_table.sql
│
└── .env
```

## Description

The project follows an ETL pipeline to process data from external APIs and load it into a PostgreSQL database. The main steps are:

1. **Extraction**: Fetch data from APIs for products, carts, and users.
2. **Transformation**: Clean and preprocess the data.
3. **Loading**: Insert the transformed data into the respective PostgreSQL tables.

The project uses Python libraries such as `pandas` for data manipulation, `requests` for API calls, and `psycopg2` for database interactions. Environment variables are managed using `python-dotenv`.

## Setup

1. Clone the repository and navigate to the project directory.
2. Create and activate a virtual environment.
3. Install the required packages using `pip install -r requirements.txt`.
4. Set up the environment variables in a `.env` file.
5. Create the database tables using the SQL scripts in the `database` directory.

## Acknowledgements

- [Fake Store API](https://fakestoreapi.com/) for providing the sample data.