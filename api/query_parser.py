class QueryParser:
    @staticmethod
    def parse(sql, params, values):
        for key in params.keys():
            if key not in values:
                raise ValueError("For each param value must be provided.")
            # @TODO refactor [Julia]
            param_type = params[key]['type']
            value = values[key]
            if param_type == 'int':
                if not isinstance(value, int):
                    raise ValueError(
                        f"This value don't match the type which should be int: {key} (given value: {values[key]})")
                sql = sql.replace("{% " + f"{key}" + " %}", str(value))

            elif param_type == 'str':
                if not isinstance(value, str):
                    raise ValueError(
                        f"This value don't match the type which should be string: {key} (given value: {values[key]})")
                sql = sql.replace("{% " + f"{key}" + " %}", f'"{value}"')
            else:
                raise ValueError(f"This type is not allowed: {param_type}")

        return sql
