import pytest
from api.saved_query_repository import SavedQueryRepository


@pytest.fixture
def saved_queries_fixture():
    fixture = {
      "bigquery": [
        {
          "sql": "SELECT 7 AS test;",
          "slug": "fixture"
        }
      ]
    }
    return fixture

@pytest.fixture
def saved_queries_with_params_mismatch_fixture():
    fixture = {
      "bigquery": [
        {
          "sql": "SELECT {% evaluation_id %} AS test;",
          "slug": "fixture",
          "params": "some params"
        }
      ]
    }
    return fixture

@pytest.fixture
def saved_queries_with_params_fixture():
    fixture = {
      "bigquery": [
        {
          "sql": "SELECT {% evaluation_id %} AS test;",
          "slug": "fixture",
          "params": {
              "evaluation_id": {
                  "type": "int"
              }
          }
        }
      ]
    }
    return fixture


def test_invalid_queries(saved_queries_with_params_mismatch_fixture):
    with pytest.raises(ValueError):
        SavedQueryRepository(saved_queries_with_params_mismatch_fixture)


def test_valid_queries(saved_queries_with_params_fixture):
    SavedQueryRepository(saved_queries_with_params_fixture)


def test_get_sql_slug_exists(saved_queries_fixture):
    slug = "fixture"
    assert SavedQueryRepository(saved_queries_fixture).get_sql(slug) == "SELECT 7 AS test;"


def test_get_sql_slug_doesnt_exist(saved_queries_fixture):
    slug = "zupa"
    with pytest.raises(KeyError):
        SavedQueryRepository(saved_queries_fixture).get_sql(slug)


def test_get_params_no_params(saved_queries_fixture):
    slug = "fixture"
    assert SavedQueryRepository(saved_queries_fixture).get_params(slug) is None


def test_get_params_with_params_mismatch(saved_queries_with_params_mismatch_fixture):
    slug = "fixture"
    with pytest.raises(ValueError):
        SavedQueryRepository(saved_queries_with_params_mismatch_fixture).get_params(slug)


def test_get_params_with_params(saved_queries_with_params_fixture):
    slug = "fixture"
    assert SavedQueryRepository(saved_queries_with_params_fixture).get_params(slug) \
        == {"evaluation_id": {"type": "int"}}

