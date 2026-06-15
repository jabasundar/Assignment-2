# ==============================
# MARKETING CAMPAIGN DATA CLEANING
# ==============================

import pandas as pd
import numpy as np
import os

print("=== MARKETING CAMPAIGN DATA CLEANING PIPELINE STARTED ===")

# ------------------------------
# 1. LOAD DATA
# ------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "marketing_data.csv")

print("Loading dataset from:", file_path)

df = pd.read_csv(file_path)

print("\nInitial Shape:", df.shape)
print("\nColumns:", df.columns)

# ------------------------------
# 2. HANDLE MISSING VALUES
# ------------------------------

# Income is important → fill with median
if df['Income'].isnull().sum() > 0:
    df['Income'] = df['Income'].fillna(df['Income'].median())

# Drop rows with missing ID (if any)
df = df.dropna(subset=['ID'])

# ------------------------------
# 3. REMOVE DUPLICATES
# ------------------------------
before = df.shape[0]
df = df.drop_duplicates()
after = df.shape[0]

print(f"\nDuplicates removed: {before - after}")

# ------------------------------
# 4. DATA TYPE CONVERSION
# ------------------------------

# Convert date column
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], errors='coerce')

# ------------------------------
# 5. FEATURE ENGINEERING
# ------------------------------

# Age
df['Age'] = 2026 - df['Year_Birth']

# Fix unrealistic ages (optional but important)
df = df[(df['Age'] >= 18) & (df['Age'] <= 100)]

# Children
df['Children'] = df['Kidhome'] + df['Teenhome']

# Total Spend
df['Total_Spend'] = (
    df['MntWines'] +
    df['MntFruits'] +
    df['MntMeatProducts'] +
    df['MntFishProducts'] +
    df['MntSweetProducts'] +
    df['MntGoldProds']
)

# Total Purchases
df['Total_Purchases'] = (
    df['NumDealsPurchases'] +
    df['NumWebPurchases'] +
    df['NumCatalogPurchases'] +
    df['NumStorePurchases']
)

# Customer Tenure (in days)
reference_date = df['Dt_Customer'].max()
df['Customer_Tenure'] = (reference_date - df['Dt_Customer']).dt.days

# ------------------------------
# 6. SEGMENTATION (RULE BASED)
# ------------------------------

# Income Segment
df['Income_Segment'] = pd.cut(
    df['Income'],
    bins=[0, 30000, 75000, 200000],
    labels=['Low', 'Mid', 'High']
)

# High Spender (top 10%)
df['High_Spender'] = df['Total_Spend'] > df['Total_Spend'].quantile(0.90)

# Young Customer
df['Young_Customer'] = df['Age'] < 30

# Family Customer
df['Family_Customer'] = df['Children'] > 0

# Campaign Responder
df['Campaign_Responder'] = df['Response'] == 1

# High Web Engagement
df['High_Web_Engagement'] = df['NumWebVisitsMonth'] > 5

# ------------------------------
# 7. OUTLIER HANDLING (optional but good)
# ------------------------------

# Remove extreme income outliers
df = df[df['Income'] < df['Income'].quantile(0.99)]

# ------------------------------
# 8. FINAL CHECK
# ------------------------------
print("\nFinal Shape:", df.shape)
print("\nMissing Values:\n", df.isnull().sum())

# ------------------------------
# 9. SAVE CLEANED DATA
# ------------------------------
output_path = os.path.join(BASE_DIR, "cleaned_marketing_data.csv")
df.to_csv(output_path, index=False)

print("\nCleaned dataset saved to:", output_path)

print("\n=== DATA CLEANING COMPLETED SUCCESSFULLY ===")