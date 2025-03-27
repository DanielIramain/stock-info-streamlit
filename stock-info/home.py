import streamlit as st

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