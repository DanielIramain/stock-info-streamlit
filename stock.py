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

option = st.selectbox('Select an option', services['Fundamentals'])

'You selected: ', option

ticker = st.text_input('Company ticker', key='ticker')
f'Ticker selected: {st.session_state.ticker}'

api_key = st.text_input('API key', key='key', type="password")
f'API key selected: {st.session_state.key}'

class Fundamentals():
    def __init__(self, service: str, ticker: str, api_key: str):    
        self.__service = service
        self.__ticker = self.validate_ticker(ticker)
        self.__api_key = self.validate_api_key(api_key)

    @property
    def service(self):
        return self.__service

    @property
    def symbol(self):
        return self.__ticker

    @property
    def apikey(self):
        return self.__api_key

    #@ticker.setter
    #def ticker(self, new_ticker):
    #    self.__ticker = self.validate_ticker(new_ticker)

    #@api_key.setter
    #def api_key(self, new_api_key):
    #    self.__api_key = self.validate_api_key(new_api_key)

    def validate_ticker(self, ticker: str) -> str:
        try:
            new_ticker = str(ticker)

            return new_ticker
        except ValueError:
            print('The ticker must be valid')

            return new_ticker
    
    def validate_api_key(self, apikey: str) -> str:
        try:
            new_api_key = str(api_key)

            return new_api_key
        except ValueError:
            print('The apikey must be valid')

            return None

    def get_data(self):
        url = f'https://www.alphavantage.co/query?function={self.__service}&symbol={self.__ticker}&apikey={self.__api_key}'
        r = requests.get(url)
        data = r.json()

        df = pd.DataFrame.from_dict(data, orient='index')

        return df

if st.button('Obtain data'):
    fundamentals = Fundamentals(option, ticker, api_key)
    data = fundamentals.get_data()
    st.dataframe(data)