CREATE TABLE products (
    id INT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    description TEXT,
    category VARCHAR(100),
    rating_rate DECIMAL(3, 2),
    rating_count INT,
    description_sentiment DECIMAL(3, 2),
    sentiment_category VARCHAR(10)
);