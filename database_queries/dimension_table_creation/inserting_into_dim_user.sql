INSERT INTO dim_user (user_id, username, email, phone, city, street, house_number, zipcode)
SELECT 
    user_id,
    username,
    email,
    phone,
    city,
    street,
    number AS house_number,
    zipcode
FROM "user";
