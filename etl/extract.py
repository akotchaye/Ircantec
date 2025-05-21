import logging
import pandas as pd


def extract(file_path):
    # Read the dataset into memory
    data = pd.read_csv(file_path, sep=";")

    # Details about the file
    logging.info(
        "Here is a little bit of information about the data stored in the dataframe"
    )
    logging.info(
        f"There are {data.shape[0]} rows and {data.shape[1]} columns in this DataFrame."
    )
    logging.info(f"The columns in this DataFrame take the following types {data.dtypes}")

    return data
