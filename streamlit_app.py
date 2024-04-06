import streamlit as st
from transformers import pipeline

# Load the language model
model = pipeline("text-generation", model="openai-gpt")

# Load the language model for translation
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-zh-en")


# Define Streamlit app with enhanced aesthetics, additional content, and fancy styling
def main():
    # Set page title and add some styling
    st.set_page_config(
        page_title="Language Model App",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Add a title to the app
    st.title("Language Model App")

    # Add a description
    st.write(
        "Welcome to the Language Model App! This app uses a pre-trained language model to generate text based on the "
        "input you provide.")

    # Add a sidebar for user input
    with st.sidebar:
        st.subheader("Enter Your Prompt:")
        user_input = st.text_area("Type here", "Once upon a time,")

    # Translate user input if it's in Chinese
    # if user_input.strip() and 0x4e00 <= ord(user_input[0]) <= 0x9fff:
    #     user_input = translator(user_input, max_length=100)[0]["translation_text"]

    # Add a button to trigger text generation
    if st.button("Generate Text"):
        # Generate text based on user input
        generated_text = model(user_input, max_length=100)[0]["generated_text"]

        # Display the generated text
        st.subheader("Generated Text:")
        st.write(generated_text)


# Run the app
if __name__ == "__main__":
    main()
