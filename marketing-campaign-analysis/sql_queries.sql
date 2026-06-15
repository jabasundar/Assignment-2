-- ==========================================
-- Marketing Campaign Analysis SQL Queries
-- ==========================================


-- 1. Total Customers KPI
SELECT 
    COUNT(*) AS total_customers
FROM customers;



-- 2. Average Customer Income
SELECT 
    ROUND(AVG(Income),2) AS avg_income
FROM customers;



-- 3. Total Customer Spending
SELECT 
    SUM(Total_Spend) AS total_spend
FROM customers;



-- 4. Campaign Response Rate
SELECT 
    ROUND(AVG(Response)*100,2) AS response_rate_percentage
FROM customers;



-- 5. High Income Customers
SELECT 
    *
FROM customers
WHERE Income > 75000;



-- 6. Average Spending by Income Segment
SELECT 
    Income_Segment,
    ROUND(AVG(Total_Spend),2) AS average_spend
FROM customers
GROUP BY Income_Segment;



-- 7. Campaign Responders Spending Analysis
SELECT 
    Campaign_Responder,
    ROUND(AVG(Total_Spend),2) AS average_spend
FROM customers
GROUP BY Campaign_Responder;



-- 8. Top 10% High Value Customers
SELECT *
FROM customers
ORDER BY Total_Spend DESC
LIMIT (
    SELECT CAST(COUNT(*) * 0.10 AS INT)
    FROM customers
);



-- 9. Spending Pattern by Country
SELECT
    Country,
    ROUND(AVG(Total_Spend),2) AS avg_spend,
    COUNT(*) AS customers
FROM customers
GROUP BY Country
ORDER BY avg_spend DESC;



-- 10. Campaign Response by Education
SELECT
    Education,
    ROUND(AVG(Response)*100,2) AS response_rate
FROM customers
GROUP BY Education
ORDER BY response_rate DESC;



-- 11. Customer Segmentation Summary
SELECT
    Income_Segment,
    COUNT(*) AS customer_count,
    ROUND(AVG(Income),2) AS avg_income,
    ROUND(AVG(Total_Spend),2) AS avg_spend
FROM customers
GROUP BY Income_Segment;



-- 12. Channel Usage Analysis
SELECT
    ROUND(AVG(NumWebPurchases),2) AS avg_web_purchase,
    ROUND(AVG(NumStorePurchases),2) AS avg_store_purchase,
    ROUND(AVG(NumCatalogPurchases),2) AS avg_catalog_purchase
FROM customers;



-- 13. High Web Engagement Customers
SELECT *
FROM customers
WHERE NumWebVisitsMonth > 5;



-- 14. Family Customers Spending
SELECT
    Children,
    ROUND(AVG(Total_Spend),2) AS avg_spend
FROM customers
GROUP BY Children;



-- 15. Ideal Target Customer Profile
SELECT
    Age_Band,
    Income_Band,
    Country,
    ROUND(AVG(Total_Spend),2) AS avg_spend,
    ROUND(AVG(Response)*100,2) AS response_rate
FROM customers
GROUP BY 
    Age_Band,
    Income_Band,
    Country
ORDER BY avg_spend DESC;