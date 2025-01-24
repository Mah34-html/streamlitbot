import streamlit as st 

st.header('st.button')

if st.button('say hello'):
     st.write('why hello?')
else:
     st.write('goodbye')

st.write('HelloMBDIA')

# Example 2

st.subheader('Range slider')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (20.0, 80.0))
st.write('Values:', values)

# Example 4

st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value= datetime (2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

