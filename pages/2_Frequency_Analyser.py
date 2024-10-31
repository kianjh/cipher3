import streamlit as st
import pandas as pd
from pages.functions import frequency_analyser

st.title("Frequency Analyser")
txt = st.text_area("Enter text to analyze here")

result = frequency_analyser(txt)
run = st.button("Run")
if len(result) and run:
    st.dataframe(result, hide_index=True)