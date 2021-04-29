import pytest
from unittest import mock
from api.app import app
import json


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


@pytest.fixture
def payload_fixture():
    fixture = {
        "sql": "SELECT 7 AS test;",
        "data": [
            {"col 1": "7.77", "col 2": "zupa"},
            {"col 1": "15", "col 2": "grzybowa"}
        ]}
    return fixture


def test_root(client):
    res = client.get('/')
    assert res.status_code == 200
    assert res.get_data(as_text=True) == "Hello world!"


def test_index(client):
    res = client.get('/api/v1/')
    assert res.status_code == 200
    assert res.get_data(as_text=True) == "Hello world!"


def test_echo_with_no_payload(client):
    res = client.post(
        '/api/v1/echo/'
    )
    assert res.status_code == 400
    result = json.loads(res.get_data(as_text=True))
    assert 'error' in result


def test_echo_with_not_a_json_payload(client):
    res = client.post(
        '/api/v1/echo/',
        data='xxx',
        content_type='text/plain'
    )
    assert res.status_code == 400
    result = json.loads(res.get_data(as_text=True))
    assert 'error' in result


def test_echo(client):
    payload = json.dumps({"data": 2})
    res = client.post(
        '/api/v1/echo/',
        data=payload,
        content_type='application/json'
    )
    assert res.status_code == 200
    result = json.loads(res.get_data(as_text=True))
    assert result['data'] == 2

    payload = json.dumps({"datasource": "xxx"})
    res = client.post(
        '/api/v1/echo/',
        data=payload,
        content_type='application/json'
    )
    assert res.status_code == 200
    result = json.loads(res.get_data(as_text=True))
    assert result['datasource'] == "xxx"


def test_query_with_no_payload(client):
    res = client.post(
        '/api/v1/query/'
    )
    assert res.status_code == 400
    result = json.loads(res.get_data(as_text=True))
    assert 'error' in result


def test_query_with_not_a_json_payload(client):
    res = client.post(
        '/api/v1/query/',
        data='xxx',
        content_type='text/plain'
    )
    assert res.status_code == 400
    result = json.loads(res.get_data(as_text=True))
    assert 'error' in result
