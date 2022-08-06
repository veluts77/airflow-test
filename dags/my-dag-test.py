import datetime
import pendulum
import os
import re

import requests
from airflow.decorators import dag, task
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.postgres.operators.postgres import PostgresOperator


@dag(
    schedule_interval="0 0 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
)
def my_dag_test():
    create_results_table = PostgresOperator(
        task_id="create_results_table",
        postgres_conn_id="tutorial_pg_conn",
        sql="sql/results_schema.sql",
    )

    create_errors_table = PostgresOperator(
        task_id="create_errors_table",
        postgres_conn_id="tutorial_pg_conn",
        sql="sql/errors_schema.sql",
    )

    @task
    def collect_input():
        query = "SELECT * FROM test_input ti WHERE ti.processed = 0;"
        try:
            postgres_hook = PostgresHook(postgres_conn_id="tutorial_pg_conn")
            conn = postgres_hook.get_conn()
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            if len(rows) == 0:
                print("Nothing to process")
            else:
                print("Start processing")
                print(rows)
                for row in rows:
                    name = row[1] + " " + row[2]
                    if has_numbers(name):
                        error(row[0], name, cursor)
                    else:
                        good_result(name, cursor)
                    mark_row_as_processed(row[0], cursor)
                    conn.commit()
            return 0
        except Exception as e:
            return 1

    def has_numbers(input_string):
        return bool(re.search(r'\d', input_string))

    def error(idd, name, cursor):
        msg = "Found a bad name " + name + " in record " + str(idd)
        print(msg)
        query = "INSERT INTO test_errors (msg) VALUES ('" + msg + "');"
        cursor.execute(query)

    def good_result(name, cursor):
        name = name.upper()
        print("Found a good name " + name)
        query = "INSERT INTO test_results (name) VALUES ('" + name + "');"
        cursor.execute(query)

    def mark_row_as_processed(idd, cursor):
        query = "UPDATE test_input SET processed = 1 where id = " + str(idd) + ";"
        cursor.execute(query)

    @task
    def report_results():
        try:
            rows = rows_for_query("SELECT DISTINCT * FROM test_results;")
            print_rows_with_caption("Results:", rows)
            return 0
        except Exception as e:
            return 1

    @task
    def report_errors():
        # try:
            rows = rows_for_query("SELECT * FROM test_errors;")
            print_rows_with_caption("Errors:", rows)
            for row in rows:
                requests.post("http://error-service:8082/error", row[0])
            return 0
        # except Exception as e:
        #     return 1

    def rows_for_query(query):
        postgres_hook = PostgresHook(postgres_conn_id="tutorial_pg_conn")
        conn = postgres_hook.get_conn()
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows

    def print_rows_with_caption(caption, rows):
        if len(rows) == 0:
            print("Nothing to show")
        else:
            print(caption)
            for row in rows:
                print(row[0])

    [create_errors_table, create_results_table] >> collect_input() >> [report_results(), report_errors()]


dag = my_dag_test()
