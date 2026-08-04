# Retail Sales Data Lake Pipeline (AWS + PySpark + Airflow)

## 📌 Project Overview

This project demonstrates an end-to-end cloud-based data engineering pipeline using PySpark, AWS S3, AWS Glue, Athena, and Apache Airflow.

The pipeline processes retail sales data through ETL transformations, stores optimized partitioned data in Amazon S3, enables SQL analytics using Athena, and automates workflow orchestration using Apache Airflow running in Docker containers.

---

# 🏗️ Architecture

Retail CSV Dataset
↓
PySpark ETL Processing
↓
Amazon S3 Raw Layer
↓
AWS Glue ETL Job
↓
Partitioned Parquet Files in S3
↓
AWS Athena External Tables
↓
SQL Analytics
↓
Apache Airflow DAG Automation

---

# ⚙️ Tech Stack

* Python
* PySpark
* Apache Spark
* AWS S3
* AWS Glue
* AWS Athena
* Apache Airflow
* Docker
* Git & GitHub

---

# 📂 Project Structure

ecommerce-data-pipeline/

├── dags/
│   └── glue_pipeline_dag.py

├── pyspark/
│   └── etl_job.py
    └── glue_etl_job.py

├── datasets/
│   └── SampleSuperstore.csv

├── sql/
│   └── athena_queries.sql

├── screenshots/
│   ├── airflow_success.png
│   ├── airflow_logs.png
│   ├── docker_running.png
│   └── glue_success.png

├── docker-compose.yaml

└── README.md

---

# 🔄 ETL Workflow

1. Read retail sales CSV dataset using PySpark
2. Perform data cleaning and preprocessing
3. Apply transformations using Spark DataFrame APIs
4. Upload raw dataset to Amazon S3
5. Execute AWS Glue ETL job
6. Store transformed output as partitioned Parquet files in S3
7. Create external partitioned Athena tables
8. Query transformed data using Athena SQL
9. Trigger Glue ETL workflow automatically using Apache Airflow DAG

---

# 🚀 Features Implemented

* End-to-end ETL pipeline
* Cloud-based data lake architecture
* Partitioned Parquet data storage
* Athena SQL querying
* Airflow workflow orchestration
* Automated Glue job triggering
* Dockerized Airflow setup
* AWS IAM integration

---

# 📊 Data Processing Performed

* Null value handling
* Column renaming
* Data type conversion
* Data transformations
* Partitioned output generation
* Parquet optimization

---

# 📈 Partitioning Strategy

Partitioned Parquet files were used to improve Athena query performance and reduce query scan costs.

---

# 🔧 Airflow Orchestration

Apache Airflow was used to automate the ETL workflow.

The DAG:

* Triggered AWS Glue jobs using boto3
* Automated ETL execution
* Integrated AWS credentials
* Monitored execution through Airflow UI

---

# 🐳 Docker Setup

Apache Airflow services were containerized using Docker Compose.

Services used:

* Airflow Webserver
* Airflow Scheduler
* PostgreSQL
* Redis

---

# ⚠️ Challenges Faced

* Configured Airflow on Windows using Docker
* Managed AWS IAM permissions for Glue access
* Debugged Airflow DAG scheduling issues
* Configured AWS credentials inside containers
* Resolved Glue job metadata errors
* Implemented partitioned Athena tables

---

# ✅ Project Outcome

Successfully built and automated a cloud-based retail ETL pipeline integrating PySpark, AWS Glue, Athena, and Apache Airflow.


# 👤 Author

Sonia Murugesan

Built as part of a Data Engineering portfolio project.

