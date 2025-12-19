st.title("🤖 LLM Project")

# Streamlit text input instead of input()
prompt = st.text_input("Enter your prompt")

if st.button("Generate"):
    if prompt.strip():  # ensure input is not empty
        with st.spinner("Thinking..."):
            result = get_llm_response(prompt)
            st.write(result)
    else:
        st.warning("Please enter a prompt")

