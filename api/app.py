from flask import Flask, request, jsonify
from google.cloud import bigquery

from saved_query_repository import SavedQueryRepository

app = Flask(__name__)

DEFAULT_BQ_PROJECT = "staging-nomagic-ai"
LOCATION = "EU"
CLIENT = bigquery.Client(project=DEFAULT_BQ_PROJECT)


@app.route("/")
def root() -> str:
    return "Hello world!"


@app.route("/api/v1/")
def index() -> str:
    return "Hello world!"


@app.route("/api/v1/echo/", methods=['POST'])
def echo():
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400

    return jsonify(request.json)


# @TODO typing
@app.route("/api/v1/query/", methods=['POST'])
def query():
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400

    json = request.json

    if 'slug' in json:
        slug = json['slug']
        try:
            sql = SavedQueryRepository().get_sql(slug)
        except KeyError:
            return jsonify({"error": f"SQL query not found for slug {slug}."})
    elif 'sql' in json:
        sql = json['sql']
    else:
        return jsonify({"error": "SQL query not given."})

    result = get_bigquery_result(DEFAULT_BQ_PROJECT, sql).to_dataframe().to_json(orient='records')

    return jsonify({"result": result})


# it should be in a separate adapter, but so far it's just a PoT
def get_bigquery_result(project, query):
    return CLIENT.query(query, location=LOCATION).result()


def get_saved_query(payload):
    pass


if __name__ == "__main__":
    # app.run()
    app.run(host='127.0.0.1', port=5001)

