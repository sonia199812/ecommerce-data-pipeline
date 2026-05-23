# ecommerce-data-pipeline:


# Retail Sales Data Lake Pipeline (AWS + PySpark + Airflow)

## 📌 Project Overview
This project simulates a modern Data Lake architecture using PySpark for ETL processing. It processes retail sales data and prepares it for cloud-based analytics using AWS services.

---

## 🏗️ Architecture
Retail CSV Dataset  
→ S3 Raw Layer (simulated locally)  
→ PySpark ETL (Data Cleaning + Transformation)  
→ Processed Parquet Layer  
→ Athena (future step)  
→ Airflow DAG (workflow automation - planned)

---

## ⚙️ Tech Stack
- Python (used with PySpark)
- PySpark
- Apache Spark
- AWS S3, Glue, Athena (planned)
- Apache Airflow (planned)
- Git & GitHub

---

## 📂 Project Structure
pyspark/ → ETL script  
datasets/ → Raw dataset  
dags/ → Airflow workflows  
sql/ → Athena queries  
screenshots/ → Output proof  

---

## 🔄 ETL Process
1. Load CSV dataset
2. Clean null values
3. Rename columns
4. Apply transformations
5. Export processed data (CSV/Parquet)

---

## 📊 Skills Demonstrated
- Data Engineering pipeline design
- PySpark transformations
- Data cleaning & preprocessing
- Git version control
- ETL workflow understanding

---

## 🚀 Future Improvements
- Deploy on AWS EMR
- Store data in S3 buckets
- Query using Athena
- Automate using Airflow DAGs

---

## 👤 Author
Sonia Murugesan
Built as part of a Data Engineering portfolio project.
