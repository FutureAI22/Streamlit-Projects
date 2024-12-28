import streamlit as st
import pandas as pd
import numpy as np
st.title("Hello Streamlit")
st.write("This is a simple text")
df1 = pd.DataFrame({
    "Name":["Ali", "Ahmed","Mark"],
    "Age":[25,35,56],
    "Gender":["M","M","M"]
})
st.write(df1)
df2 = pd.DataFrame({
    "x":[1,2,3,4,5,6,7,8,9],
    "y":[1,4,9,16,25,36,49,64,81]
})
st.line_chart(df2)
chart_data = pd.DataFrame(
    np.random.randint(5, 50, size=(20,3)),
    columns =['a','b','c']
    )
st.write(chart_data)
st.line_chart(chart_data)

name = st.text_input("Please Enter Your Name: ")
if name:
    st.write(f"Hello {name}")