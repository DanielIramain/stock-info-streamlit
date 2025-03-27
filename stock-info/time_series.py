import streamlit as st

st.session_state.current_page = "time_series"

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
