import streamlit as st

st.set_page_config(
    page_title="Irene AI",
    page_icon="🤖"
)

st.title("🤖 Irene AI")

st.write("Welcome to my website!")

st.header("Ask a question")

name = st.text_input("What's your name?")

if name:
    st.success(f"Hello, {name}! 👋")

question = st.text_area("What would you like to ask?")

if st.button("Submit"):
    if question:
        st.info("Your question was received!")
        st.write("You asked:")
        st.write(question)
    else:
        st.warning("Please enter a question first.")
