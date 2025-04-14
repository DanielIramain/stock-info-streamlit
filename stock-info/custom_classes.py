from utils import rerun

import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
class Information():
    'Base class for obtaining information from the API'
    def __init__(self, ticker, api_key):
        self.ticker = ticker
        self.api_key = api_key

    @property
    def ticker(self):
        return self._ticker

    @property
    def api_key(self):
        return self._api_key

    @ticker.setter
    def ticker(self, new_ticker):
        try:
            if new_ticker.isdigit():
                rerun(':warning: Ticker cannot be a number. Retry with a valid ticker.')
            elif new_ticker is None or not new_ticker.strip():
                rerun(':warning: Ticker is empty. Retry with input information.')
            elif len(new_ticker) > 5:
                rerun(':warning: Ticker is too long. Retry with a valid ticker.')
            else:
                self._ticker = new_ticker.upper()
        except Exception as e:
            print(f'An error occured while setting the ticker value: {type(e).__name__}')

    @api_key.setter
    def api_key(self, new_api_key):
        try:
            if new_api_key is None or not new_api_key.strip():
                rerun(':warning: API key is empty. Retry with input information.')
            else:
                self._api_key = new_api_key
        except Exception as e:
            print(f'An error occured while setting the API key value: {type(e).__name__}')
class Fundamentals(Information):
    'Fundamental Analysis class that works with a ticker and an API key'
    def __init__(self, ticker, api_key):
        super().__init__(ticker, api_key)

    def get_overview(self):
        'Obtain overview of the company: description and indicators'
        url = f'https://www.alphavantage.co/query?function=overview&symbol={self.ticker}&apikey={self.api_key}'
        r = requests.get(url)
        data = r.json()
        df_overview = pd.DataFrame.from_dict(data, orient='index')
        resume = df_overview.loc['MarketCapitalization'::]

        df_overview.drop(resume.index.values.tolist(), inplace=True)
        
        return [df_overview, resume]

    def get_data(self, option: str):
        'Obtain financial data as DataFrame for Fundamental Analysis'

        try:
            url = f'https://www.alphavantage.co/query?function={option}&symbol={self.ticker}&apikey={self.api_key}'
            r = requests.get(url)
            data = r.json()
            
            if option in ['income_statement', 'balance_sheet', 'cash_flow']:
                if st.session_state['optional'] == 'annual':
                    df_annual = pd.DataFrame(data['annualReports'])
                    
                    return df_annual
                else:
                    df_quarterly = pd.DataFrame(data['quarterlyReports'])
                    
                    return df_quarterly
            elif option == 'earnings':
                if st.session_state['optional'] == 'annual':
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

class TimeSeries(Information):
    'Get time series of the company'
    def __init__(self, ticker, api_key, interval:str):
        super().__init__(ticker, api_key)
        self.__interval = interval

    @property
    def interval(self):
        return self.__interval

    @interval.setter
    def interval(self, new_interval):
        self.__interval = new_interval
    
    def transform_data(self, option: str):
        '''
        Transforms data depending on the service in the solicitude
        '''
        try:
            url = f'https://www.alphavantage.co/query?function={option}&symbol={self.ticker}&interval={self.__interval}&apikey={self.api_key}'
            request = requests.get(url)
            data = request.json()
            
            services = ['time_series_intraday', 
                    'time_series_daily', 
                    'time_series_weekly',
                    'time_series_weekly_adjusted',
                    'time_series_monthly',
                    'time_series_monthly_adjusted',
                    'global_quote']
            
            if option in services[0:6]:
                data_keys = list(data.keys())
                df = pd.DataFrame.from_dict(data[data_keys[1]], orient='index')

                return df
            elif option == 'global_quote':
                df = pd.DataFrame(data)

                return df
        except Exception as e:
            print(f'Error transforming time series data: {type(e).__name__}')
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