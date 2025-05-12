# import the necessary modules
from etl.load import load
from etl.extract.extract import extract
from etl.transform.transform import transform

raw_data = extract()  # Extract the data from the raw directory
cleaned_data = transform(raw_data)  # Transform the data
load()
