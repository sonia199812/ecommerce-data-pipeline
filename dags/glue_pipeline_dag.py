from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import boto3

# Function to trigger AWS Glue Job
def trigger_glue_job():
    client = boto3.client(
        'glue',
        region_name='ap-south-1'
    )

    response = client.start_job_run(
        JobName='retail_etl_glue_job'
    )

    print("Glue Job Triggered")
    print(response)

# DAG Definition
with DAG(
        dag_id='retail_glue_pipeline',
        start_date=datetime(2026, 5, 25),
        schedule='@daily',
        catchup=False
) as dag:

    run_glue_job = PythonOperator(
        task_id='trigger_glue_job',
        python_callable=trigger_glue_job
    )
