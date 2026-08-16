import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv('GROQ_API_KEY'))

def translate_text(text_to_translate, target_language='English'):
    """Sends text to Groq for translation."""
    response = client.chat.completions.create(
    model='llama-3.1-8b-instant',
    messages=[
        {
            'role':'system',
            'content': f'you are translator for {target_language} language'
        },
        {
            'role':'user',
            'content':f'{text_to_translate}'
        }],
    temperature=.5)
    
    return response.choices[0].message.content

def main():
    target = input('what language you want translated to: ')
    while True:
        user_input = input('enter text to translate: ')
        if user_input.lower().strip() in ['exit']:
            print('exiting')
            break
        translation = translate_text(user_input, target)
        print(translation)
        
main()