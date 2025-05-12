import logging
import pandas as pd

# define the load function to load the transformed data into database


def load(data, file_path):
    data.to_csv(file_path, index=False)
    # remplacer par  un logging.info
    logging.info("The transformed data has been loaded into the processed directory\n")

    # Read the data, and return the result
    loaded_dataframe = pd.read_csv(file_path, sep=";")

    logging.info(
        "The loaded DataFrame has been read from the directory for validation\n"
    )

    try:
        assert data.shape == loaded_dataframe.shape
        logging.info(
            "Success! The data have successfully been loaded and validated"
        )

    except AssertionError:
        logging.info(
            "DataFrame shape is not consistent before and after loading. Take a closer look!"
        )
