from custom_classes import Fundamentals

import streamlit as st 

services = ['income_statement', 
            'balance_sheet', 
            'cash_flow', 
            'earnings', 
            'dividends', 
            'splits']

tab_names = ['Income statement', 'Balance Sheet', 'Cash Flow', 'Earnings', 'Dividends', 'Splits']

st.subheader(':bar_chart: Fundamentals: financial statements and reports', divider=True)

st.markdown('##### Currently provides accounting and financial information about the company.')

st.markdown(':red[**Overview:**] General information about the company.')
st.markdown(':red[**Income Statement:**] Income statements for the last 5 periods.')
st.markdown(':red[**Balance Sheet:**] Balance sheets for the last 5 periods.')
st.markdown(':red[**Cash Flow:**] Financial statement showing cash flows.')
st.markdown(':red[**Earnings:**] Data on the earnings report date, earnings per share, expected EPS, and the absolute and relative "surprise" level.')
st.markdown(":red[**Dividends:**] Information on the company's dividend payments by date.")
st.markdown(":red[**Splits:**] History of the company's dividend splits.")

with st.form('Data input'):
    ticker = st.text_input('Company ticker', key='ticker')
    'The ticker of the company you need information about ([US MARKET](https://www.nasdaq.com/market-activity/stocks/screener) data only).'

    optional = st.selectbox('Select the time lapse: ', ['annual', 'quarterly'], key='optional')
    'This option modifies the information displayed according to the time period. It affects: Income Statement, Balance Sheet, Cash Flow and Earnings report.'

    api_key = st.text_input('API key', key='key', type="password")
    'The API key from [the Alpha Vantage service](https://www.alphavantage.co/support/#api-key)'

    submit = st.form_submit_button('Obtain data')

if submit:
    fundamentals = Fundamentals(ticker, api_key)
    data_overview = fundamentals.get_overview()

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.dataframe(data_overview[0])
        with col2:
            st.dataframe(data_overview[1])
    
    tabs = st.tabs(tab_names)

    for i, (tab, service) in enumerate(zip(tabs, services)):
        with tab:
            data = fundamentals.get_data(service)
            st.dataframe(data)