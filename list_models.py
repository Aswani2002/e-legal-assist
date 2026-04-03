import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=key)

print(f"Listing models for key ...{key[-4:]}")
try:
    models = list(genai.list_models())
    for m in models:
        # Check if generateContent is supported
        if 'generateContent' in m.supported_generation_methods:
            print(f"- {m.name}")
except Exception as e:
    print(f"Error: {e}")
