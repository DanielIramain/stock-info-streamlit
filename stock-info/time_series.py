from custom_classes import TimeSeries

import streamlit as st

services = [
    'time_series_intraday', 
                    'time_series_daily', 
                    'time_series_daily_adjusted',
                    'time_series_weekly',
                    'time_series_weekly_adjusted',
                    'time_series_monthly',
                    'time_series_monthly_adjusted',
                    'global_quote']

tab_names = [
    'Time Series Intraday', 
                    'Time Series Daily', 
                    'Time Series Daily Adjusted',
                    'Time Series Weekly',
                    'Time Series Weekly Adjusted',
                    'Time Series Monthly',
                    'Time Series Monthly Adjusted',
                    'Global quote']

st.subheader('Time Series: Provide global equity data in different temporal resolutions', divider=True)
st.markdown('Time series of :red[**opening, closing, high, and low prices**] along with the volume traded (includes adjusted options) with 20+ years of historical depth.')

st.markdown(':red[**Intraday**]')
st.markdown(':red[**Daily**]')
st.markdown(':red[**Daily adjusted**]')
st.markdown(':red[**Weekly**]')
st.markdown(':red[**Weekly adjusted**]')
st.markdown(':red[**Monthly**]')
st.markdown(':red[**Monthly adjusted**]')
st.markdown(':red[**Global quote (last price and volume)**]')

with st.form('Data input'):
    ticker = st.text_input('Company ticker', key='ticker')
    'The ticker of the company you need information about (US MARKET data only).'

    interval = st.selectbox('Select the time lapse: ', ['1min', '5min', '15min', '30min', '60min'], key='interval')

    api_key = st.text_input('API key', key='key', type="password")
    'The API key from the Alpha Vantage service'

    submit = st.form_submit_button('Obtain data')

if submit:
    time_series = TimeSeries(ticker, api_key, interval)
    tabs = st.tabs(tab_names)
    
    for i, (tab, service) in enumerate(zip(tabs, services)):
        with tab:
            data = time_series.transform_data(service)
            st.dataframe(data)