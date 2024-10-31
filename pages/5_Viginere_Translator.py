import streamlit as st
from pages.functions import encrypt_viginere, decrypt_viginere

st.title("Viginere Translator")
st.header("Encrypter", divider=True)

encrypt_key = st.text_input("Enter the key:", key="Encrypt Key")
encrypt_in_text = st.text_area("Enter the text:", key="Encrypt Text")
encrypt_button = st.button("Run", "Encrypt Button")

if encrypt_button:
    encrypt_out_text = encrypt_viginere(encrypt_key, encrypt_in_text)
    st.subheader("Encrypted text:", divider=True)
    encrypt_out_text

st.header("Decrypter", divider=True)

decrypt_key = st.text_input("Enter the key:", key="Decrypt Key")
decrypt_in_text = st.text_area("Enter the text:", key="Decrypt Text")
decrypt_button = st.button("Run", "Decrypt Button")

if decrypt_button:
    decrypt_out_text = decrypt_viginere(decrypt_key, decrypt_in_text)
    st.subheader("Decrypted text:", divider=True)
    decrypt_out_text