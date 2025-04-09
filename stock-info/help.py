import streamlit as st

st.title('Whats it this even about?')

st.markdown('This app is designed to help you make better financial decisions.')
st.markdown('There are many options out there to take control of your finances, but they do not suit to well when it comes to getting data to do your own analysis.')
st.markdown('This is where Stock Info comes in: with a focus on data engineering, it gets you financial information about companies you might be interested to invest in.')

st.subheader(':stars: Is this magic?', divider=True)
st.markdown('Of course not, as explained on the home page, Stock Info is NOT intended to recommend you any inversions. Its main function is to provide you with data for your own work.')

st.subheader(':memo: Restrictions on its use', divider=True)
st.markdown('According to the Alpha Vantage service documentation, the free version allows up to 25 API calls per day ' \
'to retrieve the required information. Due to this limitation, users can only make three combined requests (fundamentals and time series) per day. ' \
'You can request a premium membership in Alpha Vantage to obtain an API key free of this restriction.')

st.subheader(':scroll: Financial Documentation', divider=True)
st.markdown('You get the data... now what? If you need a detail about what are you seeing, maybe [The fundamentals documentation](https://documentation.alphavantage.co/FundamentalDataDocs/index.html) of Alpha Vantage can help you.')

st.subheader(':male-technologist: Is that all?', divider=True)
st.markdown('Nope! As mentioned, the app is still in development, so new features will be added in the near future. Stay tuned to see what is coming soon!')

st.subheader(':coffee: Support', divider=True)
st.markdown('If you like what you have seen so far, you can [support me with a coffee](https://buymeacoffee.com/daniel.iramain). Thank you for using Stock Info!')
