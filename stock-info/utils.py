import pandas as pd

def pipeline(df: pd.DataFrame, columns_list:list) -> pd.DataFrame:
    df_aux = df[columns_list]

    df.drop(columns=columns_list, inplace=True)

    for colum in df.columns:
        df[colum] = pd.to_numeric(df[colum], errors='coerce')

    df.fillna(0, inplace=True)

    df = df_aux.join(df)

    return df
