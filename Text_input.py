import streamlit as st
st.write("Text Input Demo")
name = st.text_input("Please Enter Your Name: ")
if name:
    st.write(f"Hello {name}")