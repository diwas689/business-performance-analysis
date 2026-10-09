sql
-- SQL Query: Multi-Source Data Consolidation & Business Performance Benchmarking
-- Objective: Deduplicate transaction logs and extract quarterly performance metrics
WITH CleanedTransactions AS (
    SELECT 
        transaction_id,
        customer_id,
        store_region,
        revenue,
        transaction_date,
        -- Detect and flag duplicate transactions within the database
        ROW_NUMBER() OVER (
            PARTITION BY transaction_id 
            ORDER BY transaction_date DESC
        ) as row_num
    FROM corporate_sales_db.raw_transactions
)
SELECT 
    DATEPART(quarter, transaction_date) AS fiscal_quarter,
    store_region,
    COUNT(DISTINCT customer_id) AS active_customer_base,
    SUM(revenue) AS total_gross_revenue,
    ROUND(AVG(revenue), 2) AS average_order_value,
    COUNT(transaction_id) AS total_sales_volume
FROM CleanedTransactions
WHERE row_num = 1 -- Filter out duplicate database records to ensure data integrity
  AND transaction_date BETWEEN '2025-01-01' AND '2025-12-31'
GROUP BY DATEPART(quarter, transaction_date), store_region
ORDER BY fiscal_quarter ASC, total_gross_revenue DESC;
