import requests 

import pandas as pd
import streamlit as st

ticker = st.text_input('Company ticker', key='ticker')
f'Ticker selected: {st.session_state.ticker}'

services = {
    'Overview': 'overview',
    'Income Statement': 'income_statement',
    'Balance Sheet': 'balance_sheet',
    'Cash Flow': 'cash_flow',
    'Earnings': 'earnings',
    'Dividends': 'dividends',
    'Splits': 'splits',
    'ETF Profile': 'etf_profile'
}

option = st.selectbox('Select an option', services)
'You selected: ', services[option]

optional = st.selectbox('Select the time line: ', ['annual', 'quarterly'])
'You selected: ', optional

api_key = st.text_input('API key', key='key', type="password")
f'API key selected: {st.session_state.key}'

class Fundamentals():
    'Fundamental Analysis class that works with a ticker, the service and an API key'
    def __init__(self, ticker: str, service: str, api_key: str):    
        self.__ticker = ticker
        self.__service = service
        self.__api_key = api_key

    @property
    def ticker(self):
        return self.__ticker
    
    @property
    def service(self):
        return self.__service

    @property
    def api_key(self):
        return self.__api_key

    @ticker.setter
    def ticker(self, new_ticker):
        self.__ticker = self.validate_ticker(new_ticker)

    @api_key.setter
    def api_key(self, new_api_key):
        self.__api_key = self.validate_api_key(new_api_key)

    def validate_ticker(self, ticker: str) -> str:
        try:
            new_ticker = str(ticker)

            return new_ticker
        except ValueError:
            print('The ticker must be valid')

            return new_ticker
    
    def validate_api_key(self, api_key: str) -> str:
        try:
            new_api_key = str(api_key)

            return new_api_key
        except ValueError:
            print('The apikey must be valid')

            return None

    def get_data(self):
        'Obtain financial data for Fundamental Analysis as DataFrame'
        
        url = f'https://www.alphavantage.co/query?function={self.__service}&symbol={self.__ticker}&apikey={self.__api_key}'
        r = requests.get(url)
        data = r.json()

        try:
            if services[option] ==  'overview':
                df = pd.DataFrame.from_dict(data, orient='index')

                return df
            elif services[option] in ['income_statement', 'balance_sheet', 'cash_flow']:
                if optional == 'annual':
                    df_annual = pd.DataFrame(data['annualReports'])

                    return df_annual
                else:
                    df_quarterly = pd.DataFrame(data['quarterlyReports'])
                    
                    return df_quarterly
            elif services[option] == 'earnings':
                if optional == 'annual':
                    df_annual = pd.DataFrame(data['annualEarnings'])
                
                    return df_annual
                else:
                    df_quarterly = pd.DataFrame(data['quarterlyEarnings'])

                    return df_quarterly
            elif services[option] in ['dividends', 'splits']:
                df = pd.DataFrame(data['data'])
                
                return df
            elif services[option] == 'etf_profile':
                df = pd.DataFrame.from_dict(data, orient='index')

                return df
        except Exception as e:
            print(f'Error in get_data method: {e}')

class Grapher():
    'Plot financial information'
    def __init__(self, data):
        self.__data = data

    @property
    def data(self) -> pd.DataFrame:
        "data presented as DataFrame"
        return self.__data

    def plot_line_chart(self, title: str, x_axis, y_axis, x_text: str, y_text:str):
        'Plot a line chart using "native" type provided by Streamlit'
        st.header(title)
        st.line_chart(self.data, x=x_axis, y=y_axis, x_label=x_text, y_label=y_text)
    
if st.button('Obtain data'):
    fundamentals = Fundamentals(ticker, services[option], api_key)
    data = fundamentals.get_data()
    
    graphs = Grapher(data)
    
    st.dataframe(data)

    if services[option] == 'income_statement':
        
        graphs.plot_line_chart("Revenue and cost revenue evolution", 'fiscalDateEnding', 
                               ['totalRevenue', 'costOfRevenue', 'costofGoodsAndServicesSold'], 
                               'Fiscal date ending', 'Revenue and cost expresed in dollars')

        col1, col2 = st.columns(2)

        with col1:
            data['grossProfit'] = data['grossProfit'].astype(int)
            
            graphs.plot_line_chart("Gross profit evolution", 'fiscalDateEnding', 'grossProfit', 
                                   'Fiscal date ending', 'Gross profit expressed in dollars')
            
        with col2:
            ### converts data columns to int type and makes the calculus for the gross profit margin
            data['totalRevenue'] = data['totalRevenue'].astype(int)
            data['costofGoodsAndServicesSold'] = data['costofGoodsAndServicesSold'].astype(int)
            data['grossProfitMargin'] = ((data['totalRevenue'] - data['costofGoodsAndServicesSold']) / data['totalRevenue']) * 100

            graphs.plot_line_chart("Gross profit margin evolution", 'fiscalDateEnding', 'grossProfitMargin', 
                                   'Fiscal date ending', 'Gross profit margin')