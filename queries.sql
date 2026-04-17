-- All records
SELECT * FROM sales;

-- Total revenue
SELECT SUM(quantity * price) AS total_revenue FROM sales;

-- Top product
SELECT product, SUM(quantity) as total_qty
FROM sales
GROUP BY product
ORDER BY total_qty DESC;

-- Revenue by city
SELECT city, SUM(quantity * price) as revenue
FROM sales
GROUP BY city;

-- Category-wise revenue
SELECT category, SUM(quantity * price)
FROM sales
GROUP BY category;

-- Highest order value
SELECT *, (quantity * price) as total
FROM sales
ORDER BY total DESC
LIMIT 1;

-- Average price
SELECT AVG(price) FROM sales;