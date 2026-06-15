# 📊 Marketing Campaign Analysis

## Project Overview

This project focuses on analyzing customer marketing campaign data to understand customer behavior, spending patterns, campaign performance, and customer segments.

The project uses Python for data cleaning and analysis, SQL for database management and analytical queries, and Streamlit for building an interactive dashboard.

---

# Domain

Marketing Analytics / Customer Analytics

---

# Problem Statement

A retail company has collected customer demographic details, product spending data, purchase channel information, and campaign response data.

The objective is to identify valuable customer segments, analyze campaign effectiveness, and provide insights to improve future marketing strategies.

---

# Technologies Used

* Python
* Pandas
* NumPy
* SQL
* SQLite
* Matplotlib
* Seaborn
* Streamlit

---

# Project Workflow

## 1. Data Loading and Cleaning

The marketing dataset is loaded using Python.

Data preprocessing includes:

* Handling missing values
* Data type conversion
* Removing invalid records
* Handling outliers

---

## 2. Feature Engineering

New business features were created:

### Age

Customer age calculated from birth year.

### Total Spend

Combined spending across:

* Wine products
* Fruits
* Meat products
* Fish products
* Sweet products
* Gold products

### Total Purchases

Combined purchase activity from:

* Web purchases
* Store purchases
* Catalog purchases
* Deals purchases

### Customer Segmentation

Customer groups were created based on business rules:

* High Income Customers
* Young Customers
* Campaign Responders
* High Web Engagement Customers
* Family Customers
* High Spenders

---

# SQL Database

The cleaned dataset is stored in SQLite database.

Database:

```
marketing.db
```

Table:

```
customers
```

SQL is used for:

* KPI calculations
* Customer segmentation analysis
* Campaign performance analysis
* Spending analysis

---

# SQL Analysis Performed

Queries include:

* Total customer count
* Average income
* Total spending
* Campaign response rate
* High income customer identification
* Spending by customer segment
* Campaign responder analysis
* Top spending customers
* Country-wise spending analysis
* Channel usage analysis

---

# Streamlit Dashboard

The interactive dashboard provides:

## Filters

Users can analyze customers using:

* Country
* Education
* Marital Status
* Age Band
* Income Band

## KPI Metrics

Dashboard displays:

* Total Customers
* Average Income
* Total Spend
* Campaign Response Rate

## Visualizations

Includes:

* Income Distribution
* Income vs Spending Analysis
* Customer Segment Spending
* Campaign Response Analysis

---

# Business Insights

Key findings:

* High-income customers contribute significantly higher revenue.
* Campaign responders show better engagement and spending behavior.
* Income has a positive relationship with total spending.
* Different customer segments have different purchasing patterns.
* Customer segmentation helps identify ideal marketing targets.

---

# Business Recommendations

1. Target high-income and high-spending customers for premium campaigns.

2. Use customer segmentation for personalized marketing.

3. Improve engagement strategies for low-response customers.

4. Focus on channels preferred by valuable customer segments.

5. Design campaigns based on customer demographics and purchasing behavior.

---

# Project Structure

```
marketing-campaign-analysis/

│
├── cleaned_marketing_data.csv
├── marketing.db
│
├── data_cleaning.py
├── sql_setup.py
├── sql_queries.sql
├── run_sql_queries.py
├── app.py
│
├── requirements.txt
└── README.md

```

---

# How to Run the Project

## Step 1: Install Dependencies

```
pip install -r requirements.txt
```

---

## Step 2: Create Database

Run:

```
python sql_setup.py
```

This creates:

```
marketing.db
```

and loads customer data into:

```
customers
```

table.

---

## Step 3: Test SQL Queries

Run:

```
python run_sql_queries.py
```

This executes analytical SQL queries.

---

## Step 4: Run Streamlit Dashboard

Run:

```
streamlit run app.py
```

The dashboard will open in the browser.

---

# Conclusion

This project provides an end-to-end marketing analytics solution by combining Python, SQL, and Streamlit to analyze customer behavior, campaign effectiveness, and customer segmentation for data-driven decision making.
