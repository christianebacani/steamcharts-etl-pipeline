"""
ETL Pipeline logger
"""
import pandas as pd
from datetime import datetime

def etl_pipeline_logs(job: str, job_description: str) -> None:
    """
    Record logs for every jobs executed as a workflow for the ETL Pipeline
    """
    now = datetime.now()
    current_datetime = now.strftime('%Y-%m-%d %H:%M:%S')

    current_logs = pd.read_csv('logs/logs.csv')
    initial_logs = pd.DataFrame({
        'job': [job],
        'job_description': [job_description],
        'datetime': [current_datetime]
    })

    updated_logs = pd.concat([
        current_logs,
        initial_logs
    ], ignore_index=False)
    updated_logs.to_csv('logs/logs.csv', index=False)