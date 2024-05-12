"""
 Airflow example test

"""


from airflow import DAG, Dataset
from airflow.decorators import dag, task
import pendulum
from airflow.operators.bash import BashOperator


@dag(
    dag_id="python_version_checker",
    description="This dag demonstrates the use of BashOperator to find the Python version",
    start_date=pendulum.datetime(2024, 5, 8, tz="UTC"),
    schedule="0 */2 * * *",
    tags=["airflow2.4", "python-version"],catchup=False)
def python_version_checker():

    run_this = BashOperator(
        task_id="check_python_version",
        bash_command="python3 --version",
    )

    run_this


python_version_checker()
