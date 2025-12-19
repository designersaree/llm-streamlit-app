# streamlit_app.py
import streamlit as st
from llm_helper import get_llm_response

# ----------------------------
# Page configuration
# ----------------------------
st.set_page_config(
    page_title="🤖 LLM Project",
    page_icon="🧠",
    layout="centered"
)

# ----------------------------
# Welcome text / instructions
# ----------------------------
st.markdown(
    """
    ### Welcome to the LLM Project!
    Enter your prompt below and click **Generate** to get AI responses.
    """
)

# ----------------------------
# Initialize session state for history
# ----------------------------
if 'history' not in st.session_state:
    st.session_state.history = []

# ----------------------------
# Clear history button
# ----------------------------
if st.button("Clear History"):
    st.session_state.history = []
    st.success("History cleared!")

# ----------------------------
# Prompt input
# ----------------------------
prompt = st.text_input("Enter your prompt")

# ----------------------------
# Generate button
# ----------------------------
if st.button("Generate"):
    if prompt.strip():  # Check input is not empty
        try:
            with st.spinner("Thinking..."):
                result = get_llm_response(prompt)
                st.success("Response:")
                st.write(result)

                # Save prompt and response to history
                st.session_state.history.append((prompt, result))
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a prompt")

# ----------------------------
# Display history
# ----------------------------
if st.session_state.history:
    st.markdown("---")
    st.markdown("### Previous Prompts & Responses")
    for p, r in reversed(st.session_state.history):
        st.markdown(f"**Prompt:** {p}")
        st.markdown(f"**Response:** {r}")
        st.markdown("---")



