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


def test_get_sql_slug_exists(saved_queries_fixture):
    slug = "fixture"
    assert SavedQueryRepository(saved_queries_fixture).get_sql(slug) == "SELECT 7 AS test;"


def test_get_sql_slug_doesnt_exist(saved_queries_fixture):
    slug = "zupa"
    with pytest.raises(KeyError):
        SavedQueryRepository(saved_queries_fixture).get_sql(slug)
