import streamlit as st

home_page = st.Page("pages/1_Home.py", title="Home")
frequency_analyser_page = st.Page("pages/2_Frequency_Analyser.py", title="Frequency Analyser")
caesar_translator_page = st.Page("pages/3_Caesar_Translator.py", title="Caesar Translator")
affine_translator_page = st.Page("pages/4_Affine_Translator.py", title="Affine Translator")
viginere_translator_page = st.Page("pages/5_Viginere_Translator.py", title="Viginere Translator")

navigation_bar = st.navigation({
    "Home": [home_page],
    "Tools": [frequency_analyser_page],
    "Translators": [caesar_translator_page, affine_translator_page, viginere_translator_page]
})

navigation_bar.run()