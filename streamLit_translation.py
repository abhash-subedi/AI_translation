import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from groq import Groq
import streamlit as st

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(page_title='AI Translator')

st.title('Gemini AI Translator')

# Check for API Key
client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))
if not client:
    st.error("`GEMINI_API_KEY` not found in `.env` file. Please set your API key to proceed.")
    st.stop()

def translate_text(text_to_translate, target_language='English'):
    """Sends text to Groq for translation."""
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=text_to_translate,
        config=types.GenerateContentConfig(
            system_instruction=f'you are translator for {target_language} language',
            temperature=0.5,
        ),
    )
    
    return response.text
    
target_language = st.text_input('Enter target language: ', value='English')
user_input = st.text_area('Enter text to translate: ', height=150)

if st.button('Translate', type='primary'):
    if not user_input.strip():
        st.warning('please enter text to translate before hitting translate.')
    else:
        with st.spinner('Translating'):
            try:
                translation = translate_text(user_input, target_language)
                st.subheader('Translation result: ')
                st.success(translation)
            except Exception as e:
                st.warning(f'failed due to {e} error')
                