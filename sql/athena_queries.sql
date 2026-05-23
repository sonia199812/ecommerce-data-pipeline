#database creation

CREATE DATABASE retail_db;

#table creation
CREATE EXTERNAL TABLE retail_db.sales (
    Ship_Mode string,
    Segment string,
    Country string,
    City string,
    State string,
    Postal_Code int,
    Category string,
    Sub_Category string,
    SalesAmount double,
    Quantity int,
    Discount double,
    Profit double
)
PARTITIONED BY (Region string)
STORED AS PARQUET
LOCATION 's3://retailprocesseddatasonia/processed/sales/';

#LOAD PARTITIONS
MSCK REPAIR TABLE retail_db.sales;

#VERIFY PARTITIONS
SHOW PARTITIONS retail_db.sales;

#TEST QUERY

SELECT Region, SUM(SalesAmount)
FROM retail_db.sales
GROUP BY Region;