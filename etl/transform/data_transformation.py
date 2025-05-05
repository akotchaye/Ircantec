# Data transformation

# Function to calculate the increase amount


def Increase(row_to_incease, row_of_comparison, year, value):
    result_rows = []
    for rti, roc in zip(row_to_incease, row_of_comparison):
        if roc == year:
            result_rows.append(rti + value)
        else:
            result_rows.append(rti)

    return result_rows


# Function to transform data


def transform(data):
    # update and add 325 to "montant cotisation" of year  "2014" and add 700 to "montant cotisation" of year "2020" as cot_update
    updated_cot = Increase(
        row_to_incease=data["montant_cotisation"],
        row_of_comparison=data["annee"],
        year=2014,
        value=325,
    )

    data["montant_cotisation"] = updated_cot

    updated_cot = Increase(
        row_to_incease=data["montant_cotisation"],
        row_of_comparison=data["annee"],
        year=2020,
        value=700,
    )

    data["montant_cotisation"] = updated_cot

    return data
