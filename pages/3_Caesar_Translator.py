import streamlit as st
from pages.functions import caesar_translator, brute_caesar_translator

st.title("Caesar Translator")
st.header("Known Key", divider=True)

key = st.number_input("Enter the key:", -25, 25, 0)
in_txt = st.text_area("Enter the text:", key="Normal Text")
run_normal = st.button("Run", "Normal Button")

if run_normal:

    out_txt = caesar_translator(key, in_txt)
    st.subheader("Translated text:", divider=True)
    out_txt

st.header("Brute force", divider=True)
in_txt_brute = st.text_area("Enter the text:", key="Brute Text")
run_brute = st.button("Run", "Brute Button")

if run_brute:

    out_txt_brute = brute_caesar_translator(in_txt_brute)
    st.subheader("Brute forced text", divider=True)
    st.dataframe(out_txt_brute, hide_index=True)