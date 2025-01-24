import streamlit as st 


st.header("This is a button")

if st.button ("Say hello"):
    st.write("Hello All!!")
else:
    st.write("Goodbye")