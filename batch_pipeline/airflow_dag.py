from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from compute_features import compute_features

with DAG('batch_feature_computation', start_date=datetime(2025,6,12), schedule_interval='@daily', catchup=False) as dag:
    task_compute_features = PythonOperator(
        task_id='compute_features',
        python_callable=compute_features
    )
