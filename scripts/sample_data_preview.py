import pandas as pd
import logging
import os

# Configuration du logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def preview_data(filepath: str, sep: str = ";", n_rows: int = 10):
    if not os.path.exists(filepath):
        logging.error(f"Le fichier '{filepath}' n'existe pas.")
        return

    try:
        logging.info(f"Chargement du fichier : {filepath}")
        df = pd.read_csv(filepath, sep=sep)

        logging.info(f"Aperçu des {n_rows} premières lignes :")
        print(df.head(n_rows))

        logging.info("Informations sur le dataset :")
        print(df.info())

        logging.info("Résumé statistique :")
        print(df.describe(include="all"))

    except Exception as e:
        logging.exception("Erreur lors de la lecture du fichier.", e)


#  Exemple de chemin vers un fichier dans ton projet
if __name__ == "__main__":
    data_path = "data/raw/raw_ircantec.csv"
    preview_data(data_path)
