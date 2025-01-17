import psycopg2
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

def load_data_products(product_df):
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cursor = conn.cursor()
    
    for index, row in product_df.iterrows():
        cursor.execute("""
            INSERT INTO products (product_id, title, price, description, category, rating_rate, rating_count, description_sentiment, sentiment_category)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (product_id) DO NOTHING  -- Change 'id' to 'product_id'
        """, (row['id'], row['title'], row['price'], row['description'], row['category'], row['rating_rate'], row['rating_count'], row['description_sentiment'], row['sentiment_category']))
    
    conn.commit()
    cursor.close()
    conn.close()

def load_data_carts(cart_df):
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cursor = conn.cursor()
    
    for index, row in cart_df.iterrows():
        # Check if the user_id exists in the users table
        cursor.execute("SELECT COUNT(*) FROM users WHERE user_id = %s", (row['user_id'],))
        user_exists = cursor.fetchone()[0] > 0
        
        if user_exists:
            cursor.execute("""
                INSERT INTO carts (cart_id, user_id, date, product_id, quantity)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (cart_id, product_id) DO NOTHING
            """, (row['cart_id'], row['user_id'], row['date'], row['product_id'], row['quantity']))
        else:
            print(f"User  ID {row['user_id']} does not exist. Skipping cart entry.")

    conn.commit()
    cursor.close()
    conn.close()

def load_data_users(user_df):
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cursor = conn.cursor()
    
    for index, row in user_df.iterrows():
        cursor.execute("""
            INSERT INTO users (user_id, email, username, password, firstname, lastname, phone, city, street, number, zipcode)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (user_id) DO NOTHING
        """, (row['user_id'], row['email'], row['username'], row['password'], row['firstname'], row['lastname'], row['phone'], row['city'], row['street'], row['number'], row['zipcode']))
    
    conn.commit()
    cursor.close()
    conn.close()