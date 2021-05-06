import re
from dataclasses import dataclass

# https://docs.python.org/3/library/dataclasses.html
@dataclass
class SavedQueryParam:
    """Class for params for queries saved in repo."""
    type: str


@dataclass
class SavedQueries:
    """Class for queries saved in repo."""
    slug: str
    sql: str
    params: SavedQueryParam = None

    # function def example, getters should probably be here [Julia]
    # def total_cost(self) -> float:
    #     return self.unit_price * self.quantity_on_hand


SAVED_QUERIES = {
  "bigquery": [
    {
      "slug": "kpi-competec-lab", # OPTIONAL, maybe different identifiers possible
      "sql": """
            SELECT robot_name, evaluation_id, all_requests, injection_success_rate, soft_failure_rate hard_failure_rate 
            FROM `staging-nomagic-ai.kpi_v2.kpi_competec`
            ORDER BY evaluation_id DESC 
            LIMIT 100;
        """ # REQUIRED
    }
  ]
}

class SavedQueryRepository:
    def __init__(self, saved_queries=SAVED_QUERIES):
        self._validate(saved_queries)
        # @TODO save it as a dataclass [Julia]
        # https://pypi.org/project/dataclasses-json/https://pypi.org/project/dataclasses-json/
        self.saved_queries = saved_queries

    def get_sql(self, slug):
        record = self._get_query_by_slug(slug)
        return record["sql"]

    def get_params(self, slug):
        record = self._get_query_by_slug(slug)
        return record["params"] if "params" in record else None

    def _get_query_by_slug(self, slug):
        for record in self.saved_queries["bigquery"]:
            if "slug" in record and record["slug"] == slug:
                return record
        raise KeyError("Query not found") # probably better exception exists

    @staticmethod
    def _validate(saved_queries):
        for query in saved_queries["bigquery"]:
            sql = query["sql"]
            expected_params = re.findall(r"{% \S+ %}", sql)
            for expected_param in expected_params:
                # @TODO refactor a bit [Julia]
                expected_param = re.sub(r"{% ", "", expected_param)
                expected_param = re.sub(r" %}", "", expected_param)
                if "params" not in query:
                    raise ValueError("No specification for query params. Please add the 'params' section.")
                if expected_param not in query["params"]:
                    raise ValueError(f"No specification for this param: {expected_param}. "
                                     f"Please add it to the 'params' section.")
