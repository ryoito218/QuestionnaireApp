import streamlit as st

st.title("Hello Streamlit!")

st.write("This is a simple Strealit app")

name = st.text_input("Enter your name")

if st.button("Greet"):
    st.write(f"Hello, {name}")