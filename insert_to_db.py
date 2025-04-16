import sqlite3
import pandas as pd

# Load the cleaned CSV data
data = pd.read_csv(r"D:\python\flaskproject\data_preprocessing\cleaned_amazon.csv")

# Connect to SQLite database (this will create the database file if it doesn't exist)
conn = sqlite3.connect("amazon_products.db")
cursor = conn.cursor()

# Create table in the SQLite database (if it doesn't already exist)
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS products (
    product_id TEXT PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    discounted_price REAL,
    actual_price REAL,
    discount_percentage REAL,
    rating REAL,
    rating_count INTEGER,
    about_product TEXT,
    user_id TEXT,
    user_name TEXT,
    review_id TEXT,
    review_title TEXT,
    review_content TEXT,
    img_link TEXT,
    product_link TEXT
)
"""
)

# Insert cleaned data into the products table
data.to_sql("products", conn, if_exists="replace", index=False)

# Commit and close the connection
conn.commit()
conn.close()

print("Data has been successfully inserted into the database.")
