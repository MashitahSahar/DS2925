import streamlit as st

# Title of the app
st.title("My First Streamlit App")

# Text input
name = st.text_input("Enter your name:")

# Number input
age = st.number_input("Enter your age:", min_value=1, max_value=120, step=1)

# Button
if st.button("Submit"):
    st.write(f"Hello, {name}! 👋")
    st.write(f"You are {age} years old.")
