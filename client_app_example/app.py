from flask import Flask, render_template
import requests
import pandas as pd
from modules.table import Table
import json

app = Flask(__name__)

API_URL = "http://127.0.0.1:5001"

ENDPOINT_ROOT = "/api/v1/"
ENDPOINT_ECHO = f"{ENDPOINT_ROOT}echo/"
ENDPOINT_BQ = f"{ENDPOINT_ROOT}query/"
ENDPOINT_TABLE = f"{ENDPOINT_ROOT}table/"


@app.route('/', methods=['GET'])
def hello():

    # res = requests.post(
    #     f"{API_URL}{ENDPOINT_BQ}",
    #     json={"sql": "SELECT 7 AS test UNION ALL SELECT 8 AS test;"}
    # )

    res1 = requests.post(
        f"{API_URL}{ENDPOINT_BQ}",
        json={"slug": "kpi-competec-lab", "values": {"evaluation_id": 3660}}
    )

    res1_json = json.loads(res1.text)
    if 'result' in res1_json:
        query_result = json.loads(res1_json['result'])
        df1 = pd.DataFrame(query_result)
        table1_html = Table.simple(df1)
    #
    # res2 = requests.post(
    #     f"{API_URL}{ENDPOINT_BQ}",
    #     json={"slug": "kpi-competec-lab-all"}
    # )
    #
    # res2_json = json.loads(res2.text)
    # if 'result' in res2_json:
    #     query_result = json.loads(res2_json['result'])
    #     df2 = pd.DataFrame(query_result)
    #     table2_html = Table.simple(df2)

    return render_template(
        'hello.html',
        query1_res=res1.text,
        table1=table1_html,
        #query2_res=res2.text,
        #table2=table2_html
    )


if __name__ == "__main__":
    app.run()
