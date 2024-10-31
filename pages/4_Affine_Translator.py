import streamlit as st
from pages.functions import encrypt_affine, decrypt_affine

st.title("Affine Translator")
st.header("Encrypter", divider=True)

encrypt_coefficent = st.number_input("Enter the coefficent:", step=1, key="Encrypt Coefficent")
encrypt_constant = st.number_input("Enter the constant:", step=1, key="Encrypt Constant")
encrypt_text = st.text_area("Enter the text:", key="Encrypt Text")
encrypt_button = st.button("Run", "Encrypt Button")

if encrypt_button:

    encrypt_out_text = encrypt_affine(encrypt_coefficent, encrypt_constant, encrypt_text)
    st.subheader("Encrypted text", divider=True)
    encrypt_out_text

st.header("Decrypter", divider=True)

decrypt_coefficent = st.number_input("Enter the coefficent:", step=1, key="Decrypt Coefficent")
decrypt_constant = st.number_input("Enter the constant:", step=1, key="Decrypt Constant")
decrypt_text = st.text_area("Enter the text:", key="Decrypt Text")
decrypt_button = st.button("Run", "Decrypt Button")

if decrypt_button:

    decrypt_out_text = decrypt_affine(decrypt_coefficent, decrypt_constant, decrypt_text)
    st.subheader("Decrypted text", divider=True)
    decrypt_out_text