"""
ETL Pipeline logger

This utility generate logs while processing data from the
Steam Charts website. The provide auditing and logs to support
troubleshooting of the ETL Pipeline.

Main function:
- `etl_pipeline_logs()` - Generate logs for ETL pipeline jobs
"""
import pandas as pd
from datetime import datetime

def etl_pipeline_logs(job: str, job_description: str, status: str, error_message: str) -> None:
    """
    ETL Pipeline logger to record the logs after executing pipeline job using different functions
    from different modules inside the package of  `etl/extract/`, `etl/transform/`, and `etl/load/`.

    :param job: ETL Pipeline job to record the logs: `Extract/Transform/Load`
    :type job: str

    :param job_description: Description of the ETL Pipeline job
    :type job_description: str

    :param status: The status after performing the job: `Successful/Failed`
    :type status: str

    :param error_message: The error messsage that indicates the proper description
        on why does the ETL Pipeline job failed
    :type error_message: str
    """
    now = datetime.now()
    timestamp = datetime.strftime("%Y-%m-%d %H:%M:%s")

    current_logs = pd.read_csv('logs/logs.csv')
    initial_logs = pd.DataFrame({
        "job": [job],
        "job_description": [job_description],
        "status": [status],
        "error_message": [error_message],
        "timestamp": [timestamp]
    })

    updated_logs = pd.concat([
        current_logs,
        initial_logs
    ], ignore_index=False)
    updated_logs.to_csv('logs/logs.csv', index=False)