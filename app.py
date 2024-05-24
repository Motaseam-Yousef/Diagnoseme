import openai
import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
openai_api = os.getenv('OPENAI_API')
if openai_api is None:
    raise Exception("API key not loaded. Check your .env file and the name of the environment variable.")

# Configure the OpenAI client with your API key
openai.api_key = openai_api

def chatbot():
    st.title("Medical Consultant Chatbot")
    st.write("You are chatting with a medical consultant. Describe your symptoms or feelings to get a diagnosis and advice. Type 'quit' to stop.")

    # Initialize session state to store messages if it's not already initialized
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # Using a form for better input handling
    with st.form("user_input_form"):
        user_input = st.text_input("You:", key="user_input")
        submit_button = st.form_submit_button("Send")

    if submit_button and user_input:
        # Append user message to conversation history
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Simulate a chat interaction
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=st.session_state.messages
        )

        # Extract content from OpenAI's response
        chat_message = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": chat_message})

    # Display all messages in the chat
    for message in st.session_state.messages:
        role = "You:" if message["role"] == "user" else "Assistant:"
        st.text_area("", value=f"{role} {message['content']}", height=100, disabled=True)

if __name__ == "__main__":
    chatbot()
