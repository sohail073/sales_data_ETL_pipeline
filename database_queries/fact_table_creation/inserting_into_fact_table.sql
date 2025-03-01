INSERT INTO fact_cart_sales (cart_id, user_id, product_id, date_id, quantity)
SELECT 
    c.cart_id,
    c.user_id,
    c.product_id,
    d.date_id,
    c.quantity
FROM carts c
JOIN dim_date d ON c.date = d.full_date;
