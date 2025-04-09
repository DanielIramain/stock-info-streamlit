import streamlit as st

st.title('_Stock Info_')
st.header(':red[Historical financial market data]')

st.markdown("Obtain financial information from publicly traded companies "
"in the U.S. stock market through [Alpha Vantage's](https://www.alphavantage.co/) API.")

st.markdown('The data is displayed as a DataFrame and can be download in .csv format to be further processed '
'either by DBMS or business intelligence platforms such as Power BI or even spreadsheets such as Excel.')

st.image('../resources/finance-home.jpg')

st.subheader('Instructions', divider=True)

st.markdown('1. Write the ticker you need. You can consult the list of [availables companies](https://www.nasdaq.com/market-activity/stocks/screener).')
st.markdown('2. Select the periodicity you need to analyse (annual or quarterly according to GAAP or IFRS for foreign companies that choose not to file with GAAP).')
st.markdown('3. Introduce your API Key from Alpha Vantage service. If you do not have one you can [claim it **FOR FREE**](https://www.alphavantage.co/support/#api-key).')