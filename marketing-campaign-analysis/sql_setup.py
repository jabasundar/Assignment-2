import pandas as pd
import sqlite3
import os

print("=== LOADING DATA INTO SQL DATABASE ===")

# ALWAYS point to project folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(BASE_DIR, "cleaned_marketing_data.csv")
db_path = os.path.join(BASE_DIR, "marketing.db")  # 🔥 IMPORTANT FIX

df = pd.read_csv(file_path)

conn = sqlite3.connect(db_path)

df.to_sql("customers", conn, if_exists="replace", index=False)

conn.close()

print("Database created at:", db_path)