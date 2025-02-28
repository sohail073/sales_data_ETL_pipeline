CREATE TABLE users (
    user_id INT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    firstname VARCHAR(100),
    lastname VARCHAR(100),
    phone VARCHAR(15),
    city VARCHAR(100),
    street VARCHAR(100),
    number VARCHAR(10),
    zipcode VARCHAR(10)
);