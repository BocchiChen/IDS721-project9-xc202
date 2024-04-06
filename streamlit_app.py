import streamlit as st
from transformers import pipeline

# Load the ChatGPT conversational model
model = pipeline("conversational", model="microsoft/DialoGPT-large")

# Load the language model for translation
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-zh-en")


# Define Streamlit app with enhanced aesthetics, additional content, and fancy styling
def main():
    # Set page title and add some styling
    st.set_page_config(
        page_title="Conversational Model App",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Add a title to the app
    st.title("Conversational Model App")
    st.markdown("---")

    # Add a description
    st.write(
        "Welcome to the Conversational Model App! This app uses a pre-trained conversational model to provide "
        "responses based on your input.")

    # Add a sidebar for user input
    with st.sidebar:
        st.subheader("Enter Your Prompt:")
        user_input = st.text_area("Type here", "Hi, how are you?")

    # Translate user input if it's in Chinese
    if user_input.strip() and 0x4e00 <= ord(user_input[0]) <= 0x9fff:
        user_input = translator(user_input, max_length=100)[0]["translation_text"]

    # Convert user input to conversation format
    conversation = [
        {"role": "user", "content": user_input}
    ]

    # Add a button to trigger response generation
    if st.button("🚀 Get Response"):
        # Generate response based on conversation history
        response = model(conversation)

        # Extract assistant's response
        assistant_response = ""
        for msg in response:
            if msg["role"] == "assistant":
                assistant_response = msg["content"]
                break

        # Display the assistant's response
        st.markdown("---")
        st.subheader("📣 Model's Response:")
        st.write(assistant_response)


# Run the app
if __name__ == "__main__":
    main()
