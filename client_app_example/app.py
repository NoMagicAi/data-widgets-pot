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

    res = requests.post(
        f"{API_URL}{ENDPOINT_BQ}",
        json={"slug": "kpi-competec-lab"}
    )

    table_html = ""
    res_json = json.loads(res.text)
    if 'result' in res_json:
        query_result = json.loads(res_json['result'])
        df = pd.DataFrame(query_result)
        table_html = Table.simple(df)

    return render_template('hello.html', query_res=res.text, table=table_html)


if __name__ == "__main__":
    app.run()
