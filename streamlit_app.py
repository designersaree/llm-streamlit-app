# streamlit_app.py
import streamlit as st
from llm_helper import get_llm_response

# Page configuration
st.set_page_config(page_title="LLM Project", layout="centered")

st.title("🤖 LLM Project")
st.write("Enter a prompt and get an AI response.")

# Streamlit text input
prompt = st.text_input("Enter your prompt")

# Button triggers AI response
if st.button("Generate"):
    if prompt.strip():  # Check input is not empty
        with st.spinner("Thinking..."):
            result = get_llm_response(prompt)
            st.success("Response:")
            st.write(result)
    else:
        st.warning("Please enter a prompt")


