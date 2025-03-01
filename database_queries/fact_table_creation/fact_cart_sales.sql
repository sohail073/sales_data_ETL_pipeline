CREATE TABLE fact_cart_sales (
    cart_id INT, 
    user_id INT REFERENCES dim_user(user_id),
    product_id INT REFERENCES dim_product(product_id),
    date_id INT REFERENCES dim_date(date_id),
    quantity INT,
    PRIMARY KEY (cart_id, product_id)  
);
