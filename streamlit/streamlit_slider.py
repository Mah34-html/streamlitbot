import streamlit as st 
from datetime import time, datetime

st.header("Let make different slider")

#Exemple 1

st.subheader ("Slider to select your age")

age= st.slider("How old are you?", 0, 100)
st.write ("My age is: ", age)

#Exemple 2

st.subheader("Slider to select age range: ")

age_range= st.slider("select your age range", 0, 100, (20, 50))
st.write("My age range is: ", age_range)

#Exemple 3

st.subheader("slider to select range time")

appointment= st.slider("schedule your appointment", value= (time(8,17), time(12,45)))
st.write("you're scheduled for: ", appointment)

#Exemple 4

st.subheader("slider to select datetime")

start_time=st.slider("when do you start?", value=datetime(2024, 12, 18, 12,28), format="DD/MM/YY - hh:mm")

end_time=st.slider("when do you finish?", value=datetime(2024,12,18, 12,28), format="DD:MM:YY - hh:mm")

st.write("Start time is: ", start_time)

st.write("End time is: ", end_time)