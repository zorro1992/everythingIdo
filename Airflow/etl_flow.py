from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'Big-Data-Platform',
    'depends_on_past': False,
    'start_date': datetime(2018, 3, 19),
    'email': ['data-platform@company.com'],
    'email_on_failure': 'raghunandana.sanur@company.com',
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG('ETL', default_args=default_args, schedule_interval=timedelta(hours=24*7))


t_pipeline0 = BashOperator(
    task_id='oozie_set',
    bash_command=
      """
        ssh -i ~/.ssh/company.pem.pem hadoop@10.0.247.176 \
        "cd /home/hadoop \
         && bash oozie.sh"
      """,
    dag=dag)

t_pipeline1 = BashOperator(
    task_id='oozie_01',
    bash_command=
      """
        ssh -i ~/.ssh/company.pem.pem hadoop@10.0.247.176 \
        "cd /home/data-management/data-management/company \
         && oozie import-tableList --filePath companyMed --hiveDB company --parallel 10"
      """,
    dag=dag)

t_pipeline2 = BashOperator(
    task_id='oozie_02',
    bash_command=
      """
        ssh -i ~/.ssh/company.pem.pem hadoop@x.y.z \
        "cd /home/data-management/data-management/company \
         && oozie import-tableList --filePath companyBig --hiveDB company --parallel 8"
      """,
    dag=dag)

t_pipeline3 = BashOperator(
    task_id='oozie_03',
    bash_command=
      """
        ssh -i ~/.ssh/company.pem.pem hadoop@x.y.z \
        "cd /home/data-management/data-management/company \
         && oozie import-tableList --filePath companyPartitioned --hiveDB company --datePartitionKey creation_date --monthly --incremental"
      """,
    dag=dag)

t_pipeline4 = BashOperator(
    task_id='oozie_04',
    bash_command=
      """
        ssh -i ~/.ssh/company.pem.pem hadoop@x.y.z \
        "cd /home/data-management/data-management/company \
         && oozie import-tableList --filePath companyPartitioned --hiveDB company --datePartitionKey creation_date --monthly --incremental"
      """,
    dag=dag)

t_pipeline5 = BashOperator(
    task_id='oozie_k2',
    bash_command=
      """
        ssh -i ~/.ssh/company.pem.pem hadoop@x.y.z \
        "cd /home/data-management/data-management/company \
         && oozie import-tableList --filePath k2utility --sourceDB k2analytics --hiveDB k2analytics"
      """,
    dag=dag)

t_pipeline6 = BashOperator(
    task_id='set_env',
    bash_command=
      """
        ssh -i ~/.ssh/company.pem.pem hadoop@x.y.z \
        cd $DATA_MANAGEMENT_company/ \
        OP1=/home/data-management/cron_logs/oozie_high_priority \
        mv "$OP1".log "$OP1"_"$YDATE".log \
        touch "$OP1".log
      """,
    dag=dag)

t_pipeline7 = BashOperator(
    task_id='oozie_1',
    bash_command=
      """
        ssh -i ~/.ssh/company.pem.pem hadoop@x.y.z\
            "source /home/hadoop/.bashrc \
            && cd /development/prod/oozie \
            && bash run.sh application-spark-parquet-reader.conf oozie-high-priority.json > /home/data-management/cron_logs/oozie_high_priority.log" \
        2>&1""",
    dag=dag)


t_pipeline8 = BashOperator(
    task_id='oozie_2',
    bash_command=
      """
        ssh -i ~/.ssh/company.pem.pem hadoop@x.y.z \
            "source /home/hadoop/.bashrc \
            && cd /development/prod/oozie \
            && bash run.sh application-spark-parquet-reader.conf oozie.json >> /home/data-management/cron_logs/oozie_spark_conf_jobs.log" \
        2>&1""",
    dag=dag)


t_pipeline9 = BashOperator(
    task_id='oozie_3',
    bash_command=
      """
        ssh -i ~/.ssh/company.pem.pem hadoop@x.y.z \
            "source /home/hadoop/.bashrc \
            && cd /development/prod/oozie \
            && bash run.sh application-hive-parquet-reader.conf oozie-hive-parquet-reader.json >> /home/data-management/cron_logs/oozie_hive_conf_jobs.log" \
        2>&1""",
    dag=dag)

t_pipeline0 >> t_pipeline1 >> t_pipeline2 >> t_pipeline3 >> t_pipeline4 >> t_pipeline5 >> t_pipeline6 >> t_pipeline7 >> t_pipeline8 >> t_pipeline9
