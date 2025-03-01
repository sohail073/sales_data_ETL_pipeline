INSERT INTO dim_product (product_id, title, category, price, description, rating_rate, rating_count)
SELECT 
    product_id,
    title,
    category,
    price,
    description,
    rating_rate,
    rating_count
FROM product;
