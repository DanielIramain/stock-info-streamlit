import requests 

import pandas as pd
import streamlit as st

services = {'Fundamentals': ['overview',
                            'income_statement', 
                            'balance_sheet',
                            'cash_flow',
                            'earnings',
                            'dividends',
                            'splits',
                            'etf_profile']}

option = st.selectbox(
    'Select an option',
     services['Fundamentals'])

'You selected: ', option

ticker = st.text_input('Company ticker', key='ticker')
f'Ticker selected: {st.session_state.ticker}'

api_key = st.text_input('API key', key='key', type="password")
f'API key selected: {st.session_state.key}'

def get_data():
    url = f'https://www.alphavantage.co/query?function={option}&symbol={ticker}&apikey={api_key}'
    r = requests.get(url)
    data = r.json()
    
    df = pd.DataFrame.from_dict(data, orient='index')

    return df

if st.button('Obtain data'):
    dataframe = get_data()
    st.dataframe(dataframe)