from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# 1. Create Spark Session
spark = SparkSession.builder.appName("RetailETL").getOrCreate()

# 2. Read CSV (RAW layer)
df = spark.read.csv(
    "s3a://retail-raw-data-sonia/raw/sales/SampleSuperstore.csv",
    header=True,
    inferSchema=True
)

# 3. DATA CLEANING (important step)
df_clean = df.dropna()

# 4. SIMPLE TRANSFORMATION (example)
df_transformed = df_clean.withColumnRenamed("Sales", "SalesAmount")

# 5. SHOW RESULT
df_transformed.show(5)

# 6. SCHEMA CHECK
df_transformed.printSchema()

# 7. Total sales by region
df_transformed.groupBy("Region").sum("SalesAmount").show()

# 8. Profit by category
df_transformed.groupBy("Category").sum("Profit").show()

# 9. Top selling cities
df_transformed.groupBy("City").sum("SalesAmount").show()

# 10. WRITE OUTPUT (DATA LAKE - PROCESSED LAYER)
df.write.parquet("s3a://retail-processed-data-sonia/processed/sales/")

# 11. STOP SPARK
spark.stop()