import streamlit as st
from transformers import pipeline

# Load the language model
model = pipeline("text-generation", model="openai-gpt")

# Define Streamlit app with enhanced aesthetics, additional content, and fancy styling
def main():
    # Set page title and add some styling
    st.set_page_config(
        page_title="Language Model Deployment",
        page_icon=":robot:",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # Add header with image
    header_html = """
    <div style="background-color: #2a9d8f; padding: 20px; border-radius: 10px;">
        <h1 style="color: white; text-align: center;">🤖 Streamlit App with a Hugging Face Model</h1>
    </div>
    <br />
    """
    st.markdown(header_html, unsafe_allow_html=True)

    # Add introduction section
    st.markdown("""
    <div style="background-color: #2a9d8f; padding: 20px; border-radius: 10px;">
        <p>Welcome to the Language Model Deployment app powered by Streamlit and Hugging Face Transformers!</p>
        <p>This app demonstrates the capabilities of a state-of-the-art language model for text generation.</p>
        <p>Simply enter some text in the input box below, click on the <span style="font-weight: bold;">Generate</span> button, and watch the model continue the text for you. Feel free to experiment with different prompts and see what interesting results you can get!</p>
    </div>
    """, unsafe_allow_html=True)

    # Add text input area with placeholder
    text_input = st.text_area("", height=200)

    # Add generate button with custom styling
    st.markdown("<style> .stButton button {background-color: #2a9d8f; color: white;}</style>", unsafe_allow_html=True)
    st.write("")
    if st.button("Generate", key="generate_button", help="Click to generate text"):
        if text_input:
            # Generate text with the language model
            generated_text = model(text_input, max_length=50, do_sample=True)[0]['generated_text']

            # Display generated text with styling
            # st.markdown("## Generated Text:")
            header_html = f"""
            <h1 style="color: white; text-align: center;">Generated Text</h1>
            <div>
                {generated_text}
            </div>
            """
            st.markdown(header_html, unsafe_allow_html=True)
        else:
            # Display warning if no text input
            st.warning("Please enter some text first.")

if __name__ == "__main__":
    main()