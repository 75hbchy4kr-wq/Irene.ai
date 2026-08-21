import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="Irene AI",
    page_icon="🤖"
)

st.title("🤖 Irene AI")
st.write("Ask me anything!")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

question = st.chat_input("Type your question...")

if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.responses.create(
                model="gpt-5-mini",
                input=st.session_state.messages
            )

            answer = response.output_text
            st.write(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
