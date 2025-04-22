from utils import get_resource_path

import streamlit as st

pages = [st.Page("home.py", title='Home', icon=':material/home:'), 
         st.Page("fundamentals.py", title='Fundamentals', icon=':material/finance:'), 
         st.Page("time_series.py", title='Time Series', icon=':material/trending_up:'), 
         st.Page("Help.py", title='Help', icon=':material/help:')]

pg = st.navigation(pages)

icon_path = get_resource_path('resources', 'icon-stock-info.png')
logo_path = get_resource_path('resources', 'logo-stock-info.png')

st.set_page_config(page_title="Stock Info", page_icon=icon_path)

pg.run()

st.sidebar.markdown(
    """
    <div style="position: fixed; bottom: 10px; left: 10px; display: flex; align-items: center;">
        <a href="https://github.com/DanielIramain/stock-info-streamlit" target="_blank" style="margin-right: 10px;">
            <img src="https://img.icons8.com/?size=80&id=iEBcQcM9rnZ9&format=png">
        </a>
        v1.0.0
    </div>
    """, 
    unsafe_allow_html=True
)

st.logo(logo_path, size='large', icon_image='../resources/icon-stock-info.png')

pages_style = """<style>
a:link , a:visited{
color: crimson;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: white;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
height: 4%;
background-color: crimson;
color: white;
text-align: center;
}
</style>
"""

footer = """<div class="footer">
    <p>Developed with ❤ by D. Daniel Iramain</p>
</div>
"""

st.markdown(pages_style,unsafe_allow_html=True)
st.markdown(footer,unsafe_allow_html=True)