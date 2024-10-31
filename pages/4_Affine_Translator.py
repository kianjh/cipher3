import streamlit as st
from pages.functions import encrypt_affine

st.title("Affine Translator")
st.header("Encrypter", divider=True)
encrypt_coefficent = st.number_input("Enter the coefficent:", step=1)
encrypt_constant = st.number_input("Enter the constant:", step=1)
encrypt_text = st.text_area("Enter the text to be translated:")
encrypt_button = st.button("Run", "Encrypt")
if encrypt_button:
    out_text = encrypt_affine(encrypt_coefficent, encrypt_constant, encrypt_text)
    "Encrypted text:"
    out_text