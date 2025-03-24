import streamlit as st

pages = st.navigation([st.Page("services.py"), st.Page("page_2.py")])
pages.run()
