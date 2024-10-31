import streamlit as st
from pages.functions import encrypt_affine, decrypt_affine

st.title("Affine Translator")
st.header("Encrypter", divider=True)

encrypt_coefficent = st.number_input("Enter the coefficent:", step=1, key="Encrypt Coefficent")
encrypt_constant = st.number_input("Enter the constant:", step=1, key="Encrypt Constant")
encrypt_text = st.text_area("Enter the text to be encrypted:")
encrypt_button = st.button("Run", "Encrypt Button")

if encrypt_button:

    out_text_encrypt = encrypt_affine(encrypt_coefficent, encrypt_constant, encrypt_text)
    "Encrypted text:"
    out_text_encrypt

st.header("Decrypter", divider=True)

decrypt_coefficent = st.number_input("Enter the coefficent:", step=1, key="Decrypt Coefficent")
decrypt_constant = st.number_input("Enter the constant:", step=1, key="Decrypt Constant")
decrypt_text = st.text_area("Enter the text to be decrypted:")
decrypt_button = st.button("Run", "Decrypt Button")

if decrypt_button:

    out_text_decrypt = decrypt_affine(decrypt_coefficent, decrypt_constant, decrypt_text)
    "Decrypted text:"
    out_text_decrypt