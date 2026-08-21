import streamlit as st


st.set_page_config(page_title="My AI", page_icon="🤖")

st.title("🤖 My AI")
st.write("Ask me anything!")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

question = st.chat_input("Type your question...")

if question:
    st.chat_message("user").write(question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.responses.create(
                model="gpt-5.6-mini",
                input=question
            )

            st.write(response.output_text)
