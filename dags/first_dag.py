from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta 
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

def my_first_func():
    print("excelent")

default_args = {
    'owner': 'Daulet',
    'retries': 1
}

with DAG(
    dag_id = 'my_script',
    default_args = default_args,
    start_date = datetime(2026,6,28),
    schedule_interval = '@daily',
) as dag:

    task1 = BashOperator(
        task_id = 'perv_zad',
        bash_command = 'echo "Privet"'
    )
    task2 = BashOperator(
        task_id = 'vro_zad',
        bash_command = 'date'
    )
    task3 = PythonOperator(
        task_id = 'python_task',
        python_callable = my_first_func
    )
    task4 = PostgresOperator(
        task_id = 'create_table_in_db',
        postgres_conn_id = 'postgres_default',
        sql = """
            CREATE TABLE IF NOT EXISTS my_first_table (
                id SERIAL PRIMARY KEY,
                run_date DATE NOT NULL,
                status VARCHAR(50)
            );
    """
    )


    task1 >> task2 >> task3 >> task4

