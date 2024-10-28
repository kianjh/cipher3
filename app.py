import streamlit as st

st.title("A New Website!!!")
st.header("We're brainstorming this")
st.subheader("Don't even get me started on this")
st.markdown("""
PLEASE **NO**
REALLY PLEASE NO
SAVE ME, PLEASE HELP
            """)

values = st.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))
st.write(f"Values: {values}")

st.balloons()