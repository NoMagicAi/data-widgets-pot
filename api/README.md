## API Reference

#### Hello wolrd

```http
  GET /api/v1/
```


#### Echo

```http
  POST /api/v1/echo/
```


#### Query BigQuery

```http
  POST /api/v1/query/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `slug`      | `string` | slug of a saved query |
| `sql`      | `string` | SQL to pass to BQ |
| `values`      | `string` | if query is parametrized, for each parameter value must be provided |


