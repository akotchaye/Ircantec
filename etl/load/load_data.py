import pandas as pd

# define the load function to load the transformed data into database


def load(data, file_path):
    data.to_csv(file_path, index=False)
    # remplacer par  un logging.info
    print("The transformed data has been loaded into the processed directory\n")

    # Read the data, and return the result
    loaded_dataframe = pd.read_csv(
        "C:/myproject/ircantec/data/raw/raw_ircantec.csv", sep=";"
    )

    print("The loaded DataFrame has been read from mysql for validation\n")

    try:
        assert data.shape == loaded_dataframe.shape
        print(
            "Success! The data in the table have successfully been loaded and validated"
        )

    except AssertionError:
        print(
            "DataFrame shape is not consistent before and after loading. Take a closer look!"
        )


# tester  et corriger!!!!
