import streamlit as st
from pages.functions import encrypt_viginere

st.title("Affine Translator")
st.header("Encrypter", divider=True)

encrypt_key = st.text_input("Enter the key:", key="Encrypt Key")
encrypt_in_text = st.text_area("Enter the text:", key="Encrypt Text")
encrypt_button = st.button("Run", "Encrypt Button")

if encrypt_button:
    encrypt_out_text = encrypt_viginere(encrypt_key, encrypt_in_text)
    st.subheader("Encrypted text:", divider=True)
    encrypt_out_text