import pandas as pd

#define the load function to load the transformed data into database

def load(data, file_path):
    data.to_csv(name=table_name,, index=False)
    print("Original dataframe has been loaded to mysql\n")

    # Read the data, and return the result
    loaded_dataframe = pd.read_sql(f"SELECT * FROM {table_name}", db_engine)
    print("The loaded DataFrame has been read from mysql for validation\n")

    try:
        assert dataframe.shape == loaded_dataframe.shape
        print(
            f" Success! The data in the {table_name} table have successfully been loaded and validated"
        )

    except AssertionError:
        print(
            "DataFrame shape is not consistent before and after loading. Take a closer look!"
        )

#corriger la fontion!!!!