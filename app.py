import streamlit as st
import pandas as pd
from frequency_analyser import frequency_analyser


st.title("Frequency Analyser")
txt = st.text_area(
    "Text to analyze",
    "It was the best of times, it was the worst of times, it was the age of "
    "wisdom, it was the age of foolishness, it was the epoch of belief, it "
    "was the epoch of incredulity, it was the season of Light, it was the "
    "season of Darkness, it was the spring of hope, it was the winter of "
    "despair, (...)",
)

result = frequency_analyser(txt)
df = pd.DataFrame(result).T
df.columns = ["Letter", "Count", "%"]

st.dataframe(
    df,
    hide_index=True,
    height = 900
)