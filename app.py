import streamlit as st
from openai import OpenAI
import os

# Page setup
st.set_page_config(page_title="Irene AI Chat", page_icon="🤖")
st.title("Irene AI Assistant")

# Get API key from Streamlit secrets
api_key = st.secrets.get("XAI_API_KEY")

if not api_key:
    st.error("Please add your XAI_API_KEY in Streamlit Secrets")
    st.stop()

client = OpenAI(
    api_key=api_key,
    base_url="https://api.x.ai/v1"
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are Irene, a helpful and friendly AI assistant."}
    ]

# Show previous messages
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

# User input
if prompt := st.chat_input("Ask me anything..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="grok-4.6",
                messages=st.session_state.messages,
                temperature=0.7
            )
            reply = response.choices[0].message.content
            st.markdown(reply)

    # Save AI reply
    st.session_state.messages.append({"role": "assistant", "content": reply})
