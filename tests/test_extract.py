# tests/test_extract.py
from etl.extract import extract

mock_file = "tests/fixtures/mock_data.csv"


def test_extract_returns_dataframe():
    df = extract(mock_file)
    assert df is not None
