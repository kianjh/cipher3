import streamlit as st
from pages.functions import caesar_translator, brute_caesar_translator

st.title("Caesar Translator")
st.header("Known Key", divider=True)

in_txt = st.text_area("Text to be translated here")
key = st.number_input("Enter the key here", -25, 25, 0)
run = st.button("Run", "Caesar Normal")

if run:
    out_txt = caesar_translator(key, in_txt)
    "Here is your message translated:\n"
    out_txt

st.header("Brute force", divider=True)
in_txt_brute = st.text_area("Text to be brute forced here")
run_brute = st.button("Run", "Caesar Brute")

if run_brute:
    out_txt_brute = brute_caesar_translator(in_txt_brute)
    st.dataframe(out_txt_brute, hide_index=True)