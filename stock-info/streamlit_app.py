from fundamentals import Fundamentals

import streamlit as st

pages = [st.Page("fundamentals.py", title='Fundamentals'), st.Page("time_series.py", title='Time Series')]

pg = st.navigation(pages)
pg.run()

st.title('_Stock Info_')
st.header(':red[Historical financial market data]')

st.markdown("Obtain financial information from publicly traded companies "
"in the U.S. stock market through [Alpha Vantage's](https://www.alphavantage.co/) API.")

st.markdown('The data is returned in .csv format to be further processed '
'either by DBMS or business intelligence platforms such as Power BI or even spreadsheets such as Excel.')

st.image('https://img.freepik.com/free-vector/finance-financial-performance-concept-illustration_53876-40450.jpg?t=st=1742910270~exp=1742913870~hmac=d246dc954230736a0165a981e530589243e702c1536761c93cfb88d3c6766ece&w=826')

st.subheader('Instructions', divider=True)

st.markdown('1. Write the ticker you need. You can consult the list of availables companies [here](https://www.nasdaq.com/market-activity/stocks/screener)')
st.markdown('2. Select the periodicity you need to analyse (annual or quarterly according to GAAP)')
st.markdown('3. Introduce your API KEY from Alpha Vantage service. If you do not have one: [claim it **FOR FREE** here](https://www.alphavantage.co/support/#api-key)')

st.subheader('Fundamentals: financial statements and reports', divider=True)

st.markdown('##### Currently provides accounting and financial information about the company.')

st.markdown(':red[**Overview**]: General information about the company.')
st.markdown(':red[**Income Statement**]: Income statements for the last 5 periods.')
st.markdown(':red[**Balance Sheet**]: Balance sheets for the last 5 periods.')
st.markdown(':red[**Cash Flow**]: Financial statement showing cash flows.')
st.markdown(':red[**Earnings**]: Data on the earnings report date, earnings per share, expected EPS, and the absolute and relative "surprise" level.')
st.markdown(":red[**Dividends**]: Information on the company's dividend payments by date.")
st.markdown(":red[**Splits**]: History of the company's dividend splits.")

with st.form('Data input'):
    ticker = st.text_input('Company ticker', key='ticker')
    'The ticker of the company you need information about (US MARKET data only).'

    optional = st.selectbox('Select the time lapse: ', ['annual', 'quarterly'], key='optional')
    'This option will modify the display information of time period in: income statement, balance sheet, cash flow and earnings report.'

    api_key = st.text_input('API key', key='key', type="password")
    'The API key from the Alpha Vantage service'

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