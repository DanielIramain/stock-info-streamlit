import requests 

import utils

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

services = ['income_statement', 
            'balance_sheet', 
            'cash_flow', 
            'earnings', 
            'dividends', 'splits']


ticker = st.text_input('Company ticker', key='ticker')
f'The ticker of the company you need information about'

optional = st.selectbox('Select the time line: ', ['annual', 'quarterly'])
'You selected: ', optional

api_key = st.text_input('API key', key='key', type="password")
f'The API key from the Alpha Vantage service'

class Fundamentals():
    'Fundamental Analysis class that works with a ticker, the service and an API key'
    def __init__(self, ticker: str, api_key: str):    
        self.__ticker = ticker
        self.__api_key = api_key

    @property
    def ticker(self):
        return self.__ticker

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

    def get_overview(self):
        'Obtain overview of the company: description and indicators'
        url = f'https://www.alphavantage.co/query?function=overview&symbol={self.__ticker}&apikey={self.__api_key}'
        r = requests.get(url)
        data = r.json()
        df_overview = pd.DataFrame.from_dict(data, orient='index')
        resume = df_overview.loc['MarketCapitalization'::]

        df_overview.drop(resume.index.values.tolist(), inplace=True)
        
        return [df_overview, resume]

    def get_data(self, option: str):
        'Obtain financial data as DataFrame for Fundamental Analysis'

        try:
            url = f'https://www.alphavantage.co/query?function={option}&symbol={self.__ticker}&apikey={self.__api_key}'
            r = requests.get(url)
            data = r.json()
            
            if option in ['income_statement', 'balance_sheet', 'cash_flow']:
                if optional == 'annual':
                    df_annual = pd.DataFrame(data['annualReports'])
                    
                    return df_annual
                else:
                    df_quarterly = pd.DataFrame(data['quarterlyReports'])
                    
                    return df_quarterly
            elif option == 'earnings':
                if optional == 'annual':
                    df_annual_earnings = pd.DataFrame(data['annualEarnings'])
                    
                    return df_annual_earnings
                else:
                    df_quarterly_earnings = pd.DataFrame(data['quarterlyEarnings'])
                    
                    return df_quarterly_earnings
            elif option in ['dividends', 'splits']:
                df = pd.DataFrame(data['data'])
                
                return df
            elif option == 'etf_profile':
                df = pd.DataFrame.from_dict(data, orient='index')
                
                return df
        except Exception as e:
            print(f'Error in get_data method: {type(e).__name__}')

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

    def plot_pie_chart(self, size: tuple, title: str, data: pd.DataFrame, columns: list, items_legend: list):
        'Plot a pie chart with legend'
        fig, ax = plt.subplots(figsize=size, subplot_kw=dict(aspect="equal"))

        first_row = data.iloc[0]
        df_first_row = first_row[columns]
        legend = items_legend

        def func(pct, allvals):
            absolute = int(np.round(pct/100.*np.sum(allvals)))
            return f"{pct:.1f}%\n(${absolute:d})"

        wedges, texts, autotexts = ax.pie(df_first_row, autopct=lambda pct: func(pct, df_first_row),
                                          textprops=dict(color="w"))

        ax.legend(wedges, legend,
                  title="Concepts",
                  loc="center left",
                  bbox_to_anchor=(1, 0, 0.5, 1))

        plt.setp(autotexts, size=8, weight="bold")

        ax.set_title(title)

        st.pyplot(fig)
    
if st.button('Obtain data'):
    fundamentals = Fundamentals(ticker, api_key)
    data_overview = fundamentals.get_overview()
    
    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            st.dataframe(data_overview[0])
        with col2:
            st.dataframe(data_overview[1])
        
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['Income statement', 'Balance Sheet', 'Cash Flow', 'Earnings', 'Dividends', 'Splits'])

    with tab1:
        data = fundamentals.get_data('income_statement')

        st.dataframe(data)
    with tab2:
        data = fundamentals.get_data('balance_sheet')

        st.dataframe(data)
    with tab3:
        data = fundamentals.get_data('cash_flow')

        st.dataframe(data)
    with tab4:
        data = fundamentals.get_data('earnings')

        st.dataframe(data)
    with tab5:
        data = fundamentals.get_data('dividends')

        st.dataframe(data)
    with tab6:
        data = fundamentals.get_data('splits')

        st.dataframe(data)

    #if services[option] == 'income_statement':
#
    #    data = utils.pipeline(data, ['fiscalDateEnding', 'reportedCurrency'])
    #    
    #    graphs = Grapher(data)
#
    #    graphs.plot_line_chart('Revenue and cost revenue evolution', 'fiscalDateEnding', 
    #                           ['totalRevenue', 'costOfRevenue', 'costofGoodsAndServicesSold'], 
    #                           'Fiscal date ending', 'Revenue and cost expresed in dollars')
    #    
    #    graphs.plot_line_chart('Net income evolution over time', 'fiscalDateEnding', 'netIncome', 
    #                           'Fiscal date ending', 'Net income in dollars')
    #    
    #    graphs.plot_line_chart('EBITDA evolution', 'fiscalDateEnding', 'ebitda', 'Fiscal date ending', 'EBITDA in dollars')
#
    #    col1, col2 = st.columns(2)
    #    with col1:
    #        graphs.plot_line_chart('Gross profit evolution', 'fiscalDateEnding', 'grossProfit', 
    #                               'Fiscal date ending', 'Gross profit expressed in dollars')
    #        
    #        graphs.plot_pie_chart(size=(9, 9),title='Total revenue and cost', 
    #                              data=data, columns=['totalRevenue', 'costOfRevenue'], items_legend=['Total revenue', 'Cost of revenue'])
    #        
    #    with col2:
    #        data['grossProfitMargin'] = ((data['totalRevenue'] - data['costofGoodsAndServicesSold']) / data['totalRevenue']) * 100
#
    #        graphs.plot_line_chart('Gross profit margin evolution', 'fiscalDateEnding', 'grossProfitMargin', 
    #                               'Fiscal date ending', 'Gross profit margin')
    #        
    #        graphs.plot_pie_chart(size=(9,9), title='Costs of the company', data=data, 
    #                              columns=['costofGoodsAndServicesSold', 
    #                                       'sellingGeneralAndAdministrative', 'researchAndDevelopment', 'operatingExpenses'], 
    #                              items_legend=['Cost of goods and services sold', 
    #                                            'General and administrative costs', 'R&D Cost', 'Operating expenses'])