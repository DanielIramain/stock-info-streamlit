import streamlit as st

st.title('Whats it this even about?')

st.markdown('This app is being developed to help you take better financials decisions')
st.markdown('There are many options out there to take control of your finances, but they do not suit too well when it comes to get data to make your own analysis')
st.markdown('That is where Stock Info enters in scene: with a data engineering focus, it gets you financial information about companies you could be interested to invest in')

st.subheader('Is this magic?', divider=True)
st.markdown('Of course not, as it was explicated in home page, Stock Info is NOT intended to recommend you any inversion. Its principal function is to get data for your own work.')

st.subheader('Restrictions on its use', divider=True)
st.markdown('According to the Alpha Vantage service documentation, the free version allows up to 25 API calls per day ' \
'to retrieve the required information. Because of this limitation, users can only make three combined requests (fundamentals and time series) per day. ' \
'You can request a premium membership in Alpha Vantage to obtain an API key free of this restriction.')

st.subheader('Financial Documentation', divider=True)
st.markdown('You get the data... now what? If you need a detail about what are you seeing, maybe [The fundamentals documentation](https://documentation.alphavantage.co/FundamentalDataDocs/index.html) of Alpha can help you')

st.subheader('Is that all?', divider=True)
st.markdown('Nop! As it was mentioned, the app is still in development, so it will recieve new features in the near future. Stay tune to see what is new soon!')

st.subheader('Support', divider=True)
st.markdown('If you like what you have seen so far, you can [support me with a coffee](https://buymeacoffee.com/daniel.iramain). Thank you for using Stock Info!')
