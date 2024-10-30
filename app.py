import streamlit as st

home_page = st.Page("pages/1_Home.py", title="Home")
frequency_analyser_page = st.Page("pages/2_Frequency_Analyser.py", title="Frequency Analyser")

navigation_bar = st.navigation({
    "Home": [home_page],
     "Tools": [frequency_analyser_page]
})

navigation_bar.run()