# tests/test_extract.py


def test_extract_returns_dataframe():
    from etl.extract import extract

    df = extract("C:/myproject/ircantec/data/raw/raw_ircantec.csv")
    assert df is not None
