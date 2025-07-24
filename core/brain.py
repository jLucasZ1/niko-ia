from openai import OpenAI
from dotenv import load_dotenv
import os
from core.personality import load_personality

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) # Initialize OpenAI client
personality = load_personality() #Initialize personality from core.personality

def generate_response(user_input):
    try:
        chat_response = client.chat.completions.create(
            model="gpt-3.5-turbo", # Specify the model to use
            messages=[
                {"role": "system", "content": personality["system_context"]},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7,
            max_tokens=150
        )
        return chat_response.choices[0].message.content.strip()

    except Exception as e:
        return personality["default_phrases"]["error"] + f" (erro: {e})"
