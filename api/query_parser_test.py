import pytest
from api.query_parser import QueryParser


def test_query_parser():
    QueryParser.parse(sql="", params={}, values={})
    QueryParser.parse(sql="SELECT 7;", params={}, values={})

    # for each param value must be provided
    with pytest.raises(ValueError):
        QueryParser.parse(sql="SELECT 7;", params={"evaluation_id": {"type": "int"}}, values={})
    with pytest.raises(ValueError):
        QueryParser.parse(
            sql="SELECT {% evaluation_id %};",
            params={"evaluation_id": {"type": "int"}},
            values={})

    parsed_query = QueryParser.parse(
        sql="SELECT {% evaluation_id %};",
        params={"evaluation_id": {"type": "int"}},
        values={"evaluation_id": 7})
    assert parsed_query == "SELECT 7;"

    parsed_query = QueryParser.parse(
        sql="SELECT {% evaluation_id %};",
        params={"evaluation_id": {"type": "str"}},
        values={"evaluation_id": "7"})
    assert parsed_query == "SELECT \"7\";"

    # throws when value don't match required type
    with pytest.raises(ValueError):
        QueryParser.parse(
            sql="SELECT {% evaluation_id %};",
            params={"evaluation_id": {"type": "int"}},
            values={"evaluation_id": "7"})
    with pytest.raises(ValueError):
        QueryParser.parse(
            sql="SELECT {% evaluation_id %};",
            params={"evaluation_id": {"type": "str"}},
            values={"evaluation_id": 7})

    # only int and str types are allowed ATM
    with pytest.raises(ValueError):
        QueryParser.parse(
            sql="SELECT {% evaluation_id %};",
            params={"evaluation_id": {"type": "zupa"}},
            values={"evaluation_id": 7})
