import logging
import pandas as pd


def extract():
    # Read the dataset into memory
    data = pd.read_csv("C:/myproject/ircantec/data/raw/raw_ircantec.csv", sep=";")

    # Details about the file
    print("Here is a little bit of information about the data stored in the dataframe")
    print(
        f"\nThere are {data.shape[0]} rows and {data.shape[1]} columns in this DataFrame."
    )
    print("\nThe columns in this DataFrame take the following types: ")

    # Print the type of each column
    print(data.dtypes)

    # Print a message before returning the DataFrame
    logging.info(
        "\nTo view the DataFrame extracted from 'raw directory', display the value returned by this function!\n\n"
    )
    return data

