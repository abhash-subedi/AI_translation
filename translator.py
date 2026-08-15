import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def translate_text(text_to_translate, target_language="English"):
    """Sends text to Groq for translation."""
    response = client.chat.completions.create(
    model='llama-3.1-8b-instant',
    messages=[
        {
            'role':'system',
            'content':f'translate the following message given by user into {target_language} also show roman english translation'
        },{
            'role':'user',
            'content':text_to_translate
        }
    ]
    )
    return response.choices[0].message.content
    
def main():
    
    # loop while rund while text for translation is being passed
    while True:
        text_to_translate = input('enter text to translate: ')
        if text_to_translate.lower() in ['exit']:
            print('exiting')
            break
        target_language = input('enter the target language: ')
        if target_language.lower() in ['exit']:
            print('exiting')
            break
        
        translation = translate_text(text_to_translate, target_language)
        print(translation)
        
main()