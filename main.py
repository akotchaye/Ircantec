# import the necessary modules
import logging
from etl.load import load
from etl.extract import extract
from etl.transform import transform
from etl.clean import clean


# Configuration des logs
logging.basicConfig(
    filename="logs/etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="w",  # ou "a" pour ajouter
)


def run_etl():
    logging.info("ETL has started")

    try:
        # Extraction
        logging.info("Extraction of the raw file")
        df_raw = extract("C:/myproject/ircantec/data/raw/raw_ircantec.csv")

        # Nettoyage
        logging.info("data cleanning")
        df_cleaned = clean(
            df_raw, "C:/myproject/ircantec/data/processed/cleaned_ircantec.csv"
        )

        # Transformation
        logging.info("data transformation")
        df_transfomed = transform(df_cleaned)

        # Chargement
        logging.info("data loading")
        load(df_transfomed, "C:/myproject/ircantec/data/processed/final_ircantec.csv")

        logging.info("pipeline executed with success")
    except Exception as e:
        logging.error(f"error while executing the ETL : {e}")
        raise


if __name__ == "__main__":
    run_etl()
