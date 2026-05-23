import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions
from awsglue.job import Job
from pyspark.sql.functions import col

# 1. Initialize Glue Context
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# 2. Initialize Job
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# 3. Read CSV from S3 (RAW layer)
df = spark.read.csv(
    "s3://retailrawdatasonia/raw/sales/SampleSuperstore.csv",
    header=True,
    inferSchema=True
)

# 4. DATA CLEANING
df_clean = df.dropna()

# 5. TRANSFORMATION
df_transformed = df_clean.withColumnRenamed("Sales", "SalesAmount")

# 6. SHOW SAMPLE (for logs)
df_transformed.show(5)

# 7. SCHEMA CHECK
df_transformed.printSchema()

# 8. Aggregations
df_transformed.groupBy("Region").sum("SalesAmount").show()

df_transformed.groupBy("Category").sum("Profit").show()

df_transformed.groupBy("City").sum("SalesAmount").show()

# 9. WRITE OUTPUT (PROCESSED LAYER)
df_transformed.write.mode("overwrite") \
    .partitionBy("Region") \
    .parquet("s3://retailprocesseddatasonia/processed/sales/")

# 10. Commit Job
job.commit()