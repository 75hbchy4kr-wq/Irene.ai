import streamlit as st

st.set_page_config(
    page_title="Irene AI",
    page_icon="🤖"
)

st.title("🤖 Irene AI")
st.write("Ask me anything!")

question = st.chat_input("Type your question here...")

if question:
    st.chat_message("user").write(question)

    # Temporary response
    if "hello" in question.lower():
        answer = "Hello! 👋 How can I help you?"
    elif "who are you" in question.lower():
        answer = "I'm Irene AI, your AI assistant!"
    else:
        answer = "Thanks for your question! AI responses will be connected here soon."

    st.chat_message("assistant").write(answer)
