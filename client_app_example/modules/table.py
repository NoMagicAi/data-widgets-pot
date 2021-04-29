import pandas as pd

class Table:
    def __init__(self):
        pass

    @staticmethod
    def simple(df: pd.DataFrame) -> str:
        def write_row(row):
            return f"<tr><td>{row.name}</td>" + "\n".join(
                [f"<td>{value}</td>" for key, value in row.iteritems()]) + "</tr>"

        headers = "<tr>" + "".join(f"""<th>{header}</th>""" for header in [''] + list(df.columns)) + "</tr>"
        rows = "\n".join([write_row(row) for index, row in df.iterrows()])

        html = f"""<table class="table table-striped"><thead>{headers}</thead><tbody>{rows}</tbody></table>"""
        return html




