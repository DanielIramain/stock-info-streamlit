import time

import pandas as pd
import streamlit as st


def rerun(text_warning: str) -> None:
    'Rerun the script after a few seconds.'
    st.warning(text_warning)
    
    with st.spinner(text="Please wait...", show_time=True):
        time.sleep(7)
        st.rerun()

def pipeline(df: pd.DataFrame, columns_list:list) -> pd.DataFrame:
    'Pipeline to process the data obtained from the API.'
    df_aux = df[columns_list]

    df.drop(columns=columns_list, inplace=True)

    for colum in df.columns:
        df[colum] = pd.to_numeric(df[colum], errors='coerce')

    df.fillna(0, inplace=True)

    df = df_aux.join(df)

    return df
