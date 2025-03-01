CREATE TABLE dim_product (
    product_id INT PRIMARY KEY,
    title VARCHAR(255),
    category VARCHAR(100),
    price DECIMAL(10,2),
    description TEXT,
    rating_rate DECIMAL(3,2),
    rating_count INT
);
