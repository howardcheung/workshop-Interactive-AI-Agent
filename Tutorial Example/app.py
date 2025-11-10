# app.py
import streamlit as st
from app_pocket import run_flow  # Import the direct function

st.title("Topic writer")
st.caption("Powered by Ollama + Streamlit (PocketFlow bypassed for simplicity)")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
if prompt := st.chat_input("Input a topic to write a short essay on......"):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            # Prepare messages for LLM
            llm_messages = st.session_state.messages[-1]["content"]
            output = run_flow(llm_messages)  # Direct call
            response = output["response"]
            st.write(response)
            st.session_state.messages.append({"role": "assistant", "content": response})