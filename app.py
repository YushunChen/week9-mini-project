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
    
    # Add a colorful background and customize font styles
    st.markdown(
        """
        <style>
            body {
                color: white;
                background-color: #264653;
                font-family: 'Arial', sans-serif;
            }
            .stTextInput>div>div>div>input {
                color: black;
            }
            .stButton>button {
                color: white;
                background-color: #2a9d8f;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Add header with image
    header_html = """
    <div style="background-color: #2a9d8f; padding: 20px; border-radius: 10px;">
        <h1 style="color: white; text-align: center;">🤖 Language Model Deployment with Streamlit</h1>
    </div>
    """
    st.markdown(header_html, unsafe_allow_html=True)
    
    # Add introduction section
    st.write("""
    Welcome to the Language Model Deployment app powered by Streamlit and Hugging Face Transformers! 
    This app demonstrates the capabilities of a state-of-the-art language model for text generation.
    
    Simply enter some text in the input box below, click on the "Generate" button, and watch the model 
    continue the text for you. Feel free to experiment with different prompts and see what interesting 
    results you can get!
    """)
    
    # Add text input area with placeholder and styling
    text_input = st.text_area("Enter text to generate continuation:", height=150)
    
    # Add generate button with custom styling
    if st.button("Generate", key="generate_button", help="Click to generate text"):
        if text_input:
            # Generate text with the language model
            generated_text = model(text_input, max_length=50, do_sample=True)[0]['generated_text']
            
            # Display generated text with styling
            st.markdown("## Generated Text:")
            st.write(generated_text, unsafe_allow_html=True)
        else:
            # Display warning if no text input
            st.warning("Please enter some text first.")
    
    # Add section for example generated text
    st.markdown("---")
    st.subheader("Example Generated Text:")
    examples = [
        "Once upon a time",
        "In a galaxy far, far away",
        "The quick brown fox jumps over the lazy dog"
    ]
    for example in examples:
        st.write(f"**Prompt:** {example}")
        generated_example = model(example, max_length=50, do_sample=True)[0]['generated_text']
        st.write(generated_example, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
