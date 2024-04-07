import streamlit as st
from transformers import pipeline

# Load the language model
model = pipeline("text-generation", model="openai-gpt")


# Define Streamlit app with enhanced aesthetics, additional content, and fancy styling
def main():
    # Set page title and add some styling
    st.set_page_config(
        page_title="Language Model App",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Add custom CSS styles
    st.markdown(
        """
        <style>
            .title {
                color: #1E90FF; 
                font-size: 36px; 
                text-align: center; 
                margin-bottom: 20px; 
            }

            .generated-text {
                font-size: 18px; 
                line-height: 1.5; 
                text-align: justify; 
                padding: 20px; 
                border: 5px solid #1E90FF; 
                border-radius: 10px; 
                background-color: #f8f8ff;
                box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.1); 
                color: #333333; 
            }

            .sidebar .sidebar-content {
                background-color: #f0f0f0; 
                border-radius: 10px; 
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Add a title to the app
    st.markdown("<h1 class='title'>Language Model App</h1>", unsafe_allow_html=True)
    st.markdown("---")

    # Add a description
    st.write(
        "Welcome to the Language Model App! This app uses a pre-trained language model to generate text based on the "
        "input you provide.")

    # Add a sidebar for user input
    with st.sidebar:
        st.subheader("Enter Your Prompt:")
        user_input = st.text_area("Type here in English", "Once upon a time,")

    # Add a button to trigger text generation
    if st.button("🚀 Generate Text"):
        # Generate text based on user input
        generated_text = model(user_input, max_length=100)[0]["generated_text"]

        # Display the generated text
        st.markdown("---")
        st.subheader("📣 Generated Text:")
        st.markdown("<div class='generated-text'>" + generated_text + "</div>", unsafe_allow_html=True)


# Run the app
if __name__ == "__main__":
    main()
