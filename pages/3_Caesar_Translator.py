import streamlit as st
from pages.functions import caesar_Translator

st.title("Caesar Translator")
st.header("Known Key", divider=True)

in_txt = st.text_area("Text to be translated here")
key = st.number_input("Enter the key here", -25, 25, 0)
run = st.button("Run")

if run:
    out_txt = caesar_Translator(key, in_txt)
    out_txt