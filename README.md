## Mini Project 9 - Streamlit App with a Hugging Face Model

This project is a language model application built using Streamlit and Hugging Face Transformers libraries, allowing users to generate text interactively with pretrained models. It features model selection, streamlined user interface, and can be applied in various domains like creative writing, education, and AI assistants. With continuous improvement plans, it aims to provide a seamless text generation experience for users.

### Code Overview
1. **Imports**:
    - Imported the `pipeline` function from the Streamlit library and the Hugging Face Transformers library.

2. **Load Model**:
    - Loaded a text generation model using the `pipeline("text-generation", model="openai-gpt")` statement, specifying the model as OpenAI GPT.

3. **Main Function**:
    - Defined a `main` function to build the Streamlit application.
    - Configured the page layout and styling using `st.set_page_config`.
    - Added the application title and a horizontal line using `st.title` and `st.markdown` respectively.
    - Provided a description of the application using `st.write`.
    - Created a sidebar for user input with `st.sidebar`.
        - Added a subheader and a text area for users to input text.
    - Added a button to trigger text generation using `st.button`.
    - Upon button click, generated text using the pre-trained language model and displayed it using `st.write`.

4. **Run the App**:
    - Used `if __name__ == "__main__":` to start the main function of the application.

### Project Setup
#### Requirements:

- **Streamlit:** To create the interactive web application.
- **Transformers:** For utilizing pretrained language models.
- **TensorFlow:** Required for TensorFlow-based models or operations.
- **tf-keras:** Necessary for Keras functionalities in TensorFlow.

#### Installation:

You can install the required libraries using pip:

```bash
pip install streamlit transformers tensorflow tf-keras
```

#### Usage:
Once the libraries are installed, you can start the Streamlit application locally by running:
```shell
streamlit run streamlit_app.py
```

You can use the app function by accessing the following Web URL:

![Screenshot 2024-04-06 at 12.30.38 AM.png](images%2FScreenshot%202024-04-06%20at%2012.30.38%20AM.png)

### Project Deployment on Streamlit
1. Access the official Streamlit website `https://streamlit.io/` and signin to your account.

2. Create a new app connecting to the GitHub account.

![Screenshot 2024-04-05 at 10.50.21 PM.png](images%2FScreenshot%202024-04-05%20at%2010.50.21%20PM.png)
3. Deploy the app, the process can be slow. 

![Screenshot 2024-04-05 at 10.52.18 PM.png](images%2FScreenshot%202024-04-05%20at%2010.52.18%20PM.png)

4. Once the app has been deployed, you can access the streamlit application using the web url: https://ids721-project9-xc202-a6ykzvmpybhappizrvxs5su.streamlit.app/

![Screenshot 2024-04-06 at 12.38.00 AM.png](images%2FScreenshot%202024-04-06%20at%2012.38.00%20AM.png)