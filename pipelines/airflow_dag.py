from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from src.train import train_model

with DAG(
    dag_id="house_price_training",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=['mlops']
) as dag:

    t1 = PythonOperator(
        task_id='train_model',
        python_callable=lambda: train_model(n_estimators=50)
    )

    t1
