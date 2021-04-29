import pytest
from client_app_example.modules.table import Table
import pandas as pd


@pytest.fixture
def data_fixture():
    data = {
        "col_1": ["7.77", "15"],
        "col_2": ["zupa", "grzybowa"]
    }
    return pd.DataFrame(data)


@pytest.fixture
def code_fixture():
    html = """
                <table>
                    <thead>
                        <tr><th></th><th>col_1</th><th>col_2</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>0</td><td>7.77</td><td>zupa</td></tr>
                        <tr><td>1</td><td>15</td><td>grzybowa</td></tr>
                    </tbody>
                </table>
            """
    return _remove_all_thats_white_helper(html)


def test_table_simple_not_dataframe_passed():
    with pytest.raises(Exception):
        result = Table.simple({})


def test_table_simple(data_fixture, code_fixture):


    result = Table.simple(data_fixture)
    assert _remove_all_thats_white_helper(result) == code_fixture



def _remove_all_thats_white_helper(code):
    lines = code.splitlines()
    last = lines.pop()
    code = ''.join(lines + last.splitlines())
    return code.replace(" ", "").strip()
