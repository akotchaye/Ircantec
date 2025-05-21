# tests/test_extract.py


def test_extract_returns_dataframe():
    from etl.extract import extract

    df = extract()
    assert df is not None
