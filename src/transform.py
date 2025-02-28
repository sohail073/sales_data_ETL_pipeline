from itertools import product
import pandas as pd
from textblob import TextBlob

def transform_data_products(raw_data_products):
    transformed = [
        {
            "id": item["id"],
            "title": item["title"],
            "price": item["price"],
            "description": item["description"],
            "category": item["category"],
            "rating_rate": item["rating"]["rate"],
            "rating_count": item["rating"]["count"],
        }
        for item in raw_data_products
    ]

    product_df = pd.DataFrame(transformed)

    def clean_and_preprocess_data(df):
        # Drop rows with missing values in specified columns
        df = df.dropna(subset=["id", "title", "price", "category"])  
        
        # Fill missing descriptions with a default message
        df["description"] = df["description"].fillna("No description available")  

        # Clean and preprocess the 'title' column
        df["title"] = df["title"].str.strip().str.title()

        # Clean and preprocess the 'category' column
        df["category"] = df["category"].str.lower().str.strip()

        return df

    # Call the clean_and_preprocess_data function
    product_df = clean_and_preprocess_data(product_df)

    return product_df

def transform_data_carts(raw_data_carts):
    transformed = []

    for item in raw_data_carts:
        cart_id = item["id"]
        user_id = item["userId"]
        date = item["date"]

        for product in item["products"]:
            transformed.append({
                "cart_id": cart_id,
                "user_id": user_id, 
                "date": date,
                "product_id": product["productId"],  
                "quantity": product["quantity"],
            })

    cart_df = pd.DataFrame(transformed)
    return cart_df

def transform_data_users(raw_data_users):
    transformed = []

    for item in raw_data_users:
        user_id = item["id"]
        email = item["email"]
        username = item["username"]
        password = item["password"]
        firstname = item["name"]["firstname"]
        lastname = item["name"]["lastname"]
        phone = item["phone"]
        city = item["address"]["city"]
        street = item["address"]["street"]
        number = item["address"]["number"]
        zipcode = item["address"]["zipcode"]

        transformed.append({
            "user_id": user_id,
            "email": email,
            "username": username,
            "password": password,
            "firstname": firstname,
            "lastname": lastname,
            "phone": phone,
            "city": city,
            "street": street,
            "number": number,
            "zipcode": zipcode,
        })

    # Create a DataFrame from the transformed data
    user_df = pd.DataFrame(transformed)
    return user_df