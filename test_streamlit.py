import streamlit as st

# Title of the app
st.title("Welcome to My Streamlit App")

# Input field for user's name
name = st.text_input("Enter your name:")

# Display the welcome message
if name:
    st.write(f"Hello, {name}! Welcome to the app.")

# Additional content
st.write("This is a simple Streamlit app example.")