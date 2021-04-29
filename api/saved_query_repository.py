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
        self.saved_queries = saved_queries

    def get_sql(self, slug):
        for record in self.saved_queries["bigquery"]:
            if "slug" in record and record["slug"] == slug:
                return record["sql"]
        raise KeyError("Query not found") # probably better exception exists
