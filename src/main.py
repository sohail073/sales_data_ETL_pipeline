from extract import extract_data
from transform import transform_data_products
from transform import transform_data_carts
from transform import transform_data_users
from load import load_data_products
from load import load_data_carts
from load import load_data_users
from config import PRODUCTS_API_URL
from config import CARTS_API_URL
from config import USERS_API_URL

def main():
    print("EXTRACTING.....")
    raw_data_products = extract_data(PRODUCTS_API_URL)
    raw_data_carts = extract_data(CARTS_API_URL)
    raw_data_users = extract_data(USERS_API_URL)
    print("EXTRACTION COMPLETED")

    print("TRANSFORMING.....")
    product_df = transform_data_products(raw_data_products)
    cart_df = transform_data_carts(raw_data_carts)
    user_df = transform_data_users(raw_data_users)
    print("TRANSFORMATION COMPLETED")

    print("LOADING.....")
    load_data_products(product_df)
    load_data_carts(cart_df)
    load_data_users(user_df)
    print("LOADING COMPLETED")


    

if __name__ == "__main__":
    main()