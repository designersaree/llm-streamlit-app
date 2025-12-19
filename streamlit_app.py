import streamlit as st
import os
from openai import OpenAI

st.set_page_config(page_title="LLM Project", layout="centered")

st.title("🤖 LLM Project")
st.write("Enter a prompt and get an AI response.")

# Create OpenAI client using Streamlit Secrets
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt = st.text_input("Enter your prompt")

if st.button("Generate"):
    if prompt.strip():
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            st.success("Response")
            st.write(response.choices[0].message.content)
    else:
        st.warning("Please enter a prompt")





