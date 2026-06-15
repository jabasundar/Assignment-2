import streamlit as st
import pandas as pd
import sqlite3
import os
import matplotlib.pyplot as plt

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Marketing Analytics Dashboard", layout="wide")

st.title("📊 Marketing Campaign Analytics Dashboard")
st.write("Customer segmentation, spending behavior, and campaign performance insights")

# -----------------------------
# LOAD DATA FROM SQL
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "marketing.db")

conn = sqlite3.connect(db_path)
df = pd.read_sql("SELECT * FROM customers", conn)

# -----------------------------
# FEATURE ENGINEERING
# -----------------------------
df["Age"] = 2026 - df["Year_Birth"]

df["Age_Band"] = pd.cut(
    df["Age"],
    bins=[0, 30, 45, 60, 100],
    labels=["Young", "Adult", "Middle Age", "Senior"]
)

df["Income_Band"] = pd.cut(
    df["Income"],
    bins=[0, 30000, 60000, 90000, 200000],
    labels=["Low", "Mid", "High", "Very High"]
)

# -----------------------------
# SIDEBAR FILTERS
# -----------------------------
st.sidebar.header("🔍 Filters")

country_filter = st.sidebar.multiselect(
    "Country",
    options=df["Country"].unique(),
    default=df["Country"].unique()
)

education_filter = st.sidebar.multiselect(
    "Education",
    options=df["Education"].unique(),
    default=df["Education"].unique()
)

marital_filter = st.sidebar.multiselect(
    "Marital Status",
    options=df["Marital_Status"].unique(),
    default=df["Marital_Status"].unique()
)

age_filter = st.sidebar.multiselect(
    "Age Band",
    options=df["Age_Band"].unique(),
    default=df["Age_Band"].unique()
)

income_filter = st.sidebar.multiselect(
    "Income Band",
    options=df["Income_Band"].unique(),
    default=df["Income_Band"].unique()
)
# -----------------------------
# APPLY FILTERS
# -----------------------------
df = df[
    (df["Country"].isin(country_filter)) &
    (df["Education"].isin(education_filter)) &
    (df["Marital_Status"].isin(marital_filter)) &
    (df["Age_Band"].isin(age_filter)) &
    (df["Income_Band"].isin(income_filter))
]

# -----------------------------
# SAFETY CHECK
# -----------------------------
if df.empty:
    st.error("No data available for selected filters.")
    st.stop()

# -----------------------------
# KPI CARDS
# -----------------------------
st.subheader("📌 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Customers", df.shape[0])
col2.metric("Avg Income", round(df["Income"].mean(), 2))
col3.metric("Total Spend", int(df["Total_Spend"].sum()))
col4.metric("Response Rate (%)", round(df["Response"].mean() * 100, 2))

st.markdown("---")

# -----------------------------
# CHART 1: INCOME DISTRIBUTION
# -----------------------------
st.subheader("📊 Income Distribution")

fig, ax = plt.subplots()
ax.hist(df["Income"], bins=30)
st.pyplot(fig)

# -----------------------------
# CHART 2: INCOME VS SPEND
# -----------------------------
st.subheader("💰 Income vs Spending")

fig, ax = plt.subplots()
ax.scatter(df["Income"], df["Total_Spend"])
ax.set_xlabel("Income")
ax.set_ylabel("Total Spend")
st.pyplot(fig)

# -----------------------------
# CHART 3: SEGMENT ANALYSIS
# -----------------------------
st.subheader("🧠 Income Band vs Spending")

fig, ax = plt.subplots()
df.groupby("Income_Band")["Total_Spend"].mean().plot(kind="bar", ax=ax)
st.pyplot(fig)

# -----------------------------
# CHART 4: CAMPAIGN RESPONSE
# -----------------------------
st.subheader("🎯 Campaign Response Analysis")

fig, ax = plt.subplots()
df.groupby("Response")["Total_Spend"].mean().plot(kind="bar", ax=ax)
st.pyplot(fig)

# -----------------------------
# BUSINESS INSIGHTS
# -----------------------------
st.subheader("📌 Key Business Insights")

st.markdown("""
- High-income customers contribute highest revenue
- Campaign responders show higher spending
- Age and income strongly influence spending behavior
- Mid-income group is the largest segment
- Family + married customers show different buying patterns
""")

# -----------------------------
# RAW DATA
# -----------------------------
with st.expander("🔎 View Raw Data"):
    st.dataframe(df)

conn.close()