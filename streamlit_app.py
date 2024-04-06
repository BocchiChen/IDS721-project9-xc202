import streamlit as st
from transformers import pipeline

available_models = {
    "GPT-2": "gpt2",
    "OpenAI GPT": "openai-gpt",
}

# Load the language model
default_model = available_models["OpenAI GPT"]
model = pipeline("text-generation", model=default_model)


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
    st.markdown("---")

    # Add a description
    st.write(
        "Welcome to the Language Model App! This app uses a pre-trained language model to generate text based on the "
        "input you provide.")

    # Add a sidebar for user input
    with st.sidebar:
        st.subheader("Select Model:")
        selected_model = st.selectbox("Choose a model", list(available_models.keys()), index=list(available_models.keys()).index("OpenAI GPT"))
        st.subheader("Enter Your Prompt:")
        user_input = st.text_area("Type here in English", "Once upon a time,")

    model_name = available_models[selected_model]
    text_generation_model = pipeline("text-generation", model=model_name)

    # Add a button to trigger text generation
    if st.button("🚀 Generate Text"):
        # Generate text based on user input
        generated_text = text_generation_model(user_input, max_length=100)[0]["generated_text"]

        # Display the generated text
        st.markdown("---")
        st.subheader("📣 Generated Text:")
        st.write(generated_text)


# Run the app
if __name__ == "__main__":
    main()
