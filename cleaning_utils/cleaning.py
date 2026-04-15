import pandas as pd

def clean_tshirt_categories(df, column_name="tshirt_category"):
    """
    Normalise les noms des catégories de t-shirts.
    """
    mapping = {
        "Wh Tshirt M": "White T-Shirt M",
        "Bl Tshirt M": "Black T-Shirt M",
        "Wh Tshirt F": "White T-Shirt F",
        "Bl Tshirt F": "Black T-Shirt F"
    }
    
    # On vérifie si la colonne existe pour éviter les erreurs
    if column_name in df.columns:
        df[column_name] = df[column_name].replace(mapping)
    
    return df