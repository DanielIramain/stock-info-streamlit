import streamlit as st

pages = [st.Page("home.py", title='Home'), st.Page("fundamentals.py", title='Fundamentals'), st.Page("time_series.py", title='Time Series')]

pg = st.navigation(pages)
pg.run()

# Initialize the current page in session state
st.session_state.current_page = 'streamlit_app'

st.sidebar.markdown(
    """
    <div style="position: fixed; bottom: 10px; left: 10px; display: flex; align-items: center;">
        <a href="https://github.com/DanielIramain" target="_blank" style="margin-right: 10px;">
            <img src="https://img.icons8.com/?size=80&id=iEBcQcM9rnZ9&format=png">
        </a>
        v1.0.0
    </div>
    """, 
    unsafe_allow_html=True
)

st.logo('../resources/logo-stock-info.png', size='large', icon_image='../resources/icon-stock-info.png')

footer="""<style>
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
<div class="footer">
<p>Developed with ❤ by D. Daniel Iramain</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)