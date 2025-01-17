CREATE TABLE carts (
    cart_id INT,
    user_id INT,
    date TIMESTAMP,
    product_id INT,
    quantity INT,
    PRIMARY KEY (cart_id, product_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);