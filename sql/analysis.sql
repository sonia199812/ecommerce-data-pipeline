SELECT Region, SUM(SalesAmount)
FROM retail_table
GROUP BY Region;