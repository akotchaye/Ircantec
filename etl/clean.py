import logging
import os

# raw_data = pd.read_csv("C:/myproject/ircantec/data/raw/raw_ircantec.csv", sep=";")


def clean(raw_data, file_path):
    # Check if the DataFrame is empty
    if raw_data.empty:
        logging.error("The DataFrame is empty. Please check the input data.")
        return None
    # Convert effectif_cotisants into int
    raw_data["effectif_cotisants"] = raw_data["effectif_cotisants"].astype("int")

    # Verify that effectif_cotisants is now an integer
    assert raw_data["effectif_cotisants"].dtype == "int"

    # Convert famille_d_employeurs into string
    raw_data["famille_d_employeurs"] = raw_data["famille_d_employeurs"].astype("string")

    # Verify that famille_d_employeurs is now a string
    assert raw_data["famille_d_employeurs"].dtype == "string"

    # Update '4 Hospitalière' to 'hospitalier'
    raw_data["famille_d_employeurs"] = raw_data["famille_d_employeurs"].str.replace(
        "4 Hospitalière", "hospitalier"
    )
    # Update '3 Territoriale (salariés)' to 'contractuel'
    raw_data["famille_d_employeurs"] = raw_data["famille_d_employeurs"].str.replace(
        "3 Territoriale (salariés)", "contractuel"
    )
    # Update '2 Territoriale (élus)' to 'elu'
    raw_data["famille_d_employeurs"] = raw_data["famille_d_employeurs"].str.replace(
        "2 Territoriale (élus)", "elu"
    )
    # update '1 Etat' to 'etat'
    raw_data["famille_d_employeurs"] = raw_data["famille_d_employeurs"].str.replace(
        "1 Etat", "etat"
    )
    # Update '5 Autres employeurs' to 'autre'
    raw_data["famille_d_employeurs"] = raw_data["famille_d_employeurs"].str.replace(
        "5 Autres employeurs", "autre"
    )

    # create a new column "montant cotisation" create a new copy of famille_d_employeurs then replace the values and the type of the column.
    raw_data["montant_cotisation"] = raw_data["famille_d_employeurs"]
    raw_data["montant_cotisation"] = raw_data["montant_cotisation"].str.replace(
        "hospitalier", "300000"
    )
    raw_data["montant_cotisation"] = raw_data["montant_cotisation"].str.replace(
        "contractuel", "90000"
    )
    raw_data["montant_cotisation"] = raw_data["montant_cotisation"].str.replace(
        "elu", "140000"
    )
    raw_data["montant_cotisation"] = raw_data["montant_cotisation"].str.replace(
        "etat", "54450000"
    )
    raw_data["montant_cotisation"] = raw_data["montant_cotisation"].str.replace(
        "autre", "789000"
    )
    raw_data["montant_cotisation"] = raw_data["montant_cotisation"].astype("float")

    # same for matricule
    raw_data["matricule"] = raw_data["famille_d_employeurs"]
    raw_data["matricule"] = raw_data["matricule"].str.replace("etat", "3256")
    raw_data["matricule"] = raw_data["matricule"].str.replace("elu", "4578")
    raw_data["matricule"] = raw_data["matricule"].str.replace("contractuel", "7514")
    raw_data["matricule"] = raw_data["matricule"].str.replace("hospitalier", "1021")
    raw_data["matricule"] = raw_data["matricule"].str.replace("autre", "45687")
    raw_data["matricule"] = raw_data["matricule"].astype("int")

    # save the cleaned file in the processes directory
    raw_data.to_csv(file_path, index=False)

    # Verify the persistance

    if os.path.exists(file_path):
        logging.info("Fichier persisté avec succès :", file_path)
    else:
        logging.info("Fichier non trouvé.")

    return raw_data
