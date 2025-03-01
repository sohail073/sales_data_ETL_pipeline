CREATE TABLE dim_user (
    user_id INT PRIMARY KEY,
    username VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(20),
    city VARCHAR(100),
    street VARCHAR(255),
    house_number VARCHAR(20),
    zipcode VARCHAR(20)
);
