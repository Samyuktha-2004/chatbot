import streamlit as st
from cache_code import chatbot

# Streamlit application
st.title('Chatbot Interface')

user_input = st.text_input("Enter your message:")

if user_input:
    response = chatbot(user_input)
    st.write(f"**Bot:** {response}")
