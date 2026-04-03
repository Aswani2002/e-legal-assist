import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=key)

test_models = [
    'models/gemini-2.0-flash',
    'models/gemini-2.0-flash-lite-preview-02-05',
    'models/gemini-flash-latest',
    'models/gemini-pro-latest',
]

for m_name in test_models:
    try:
        print(f"Testing {m_name}...")
        model = genai.GenerativeModel(m_name)
        response = model.generate_content("Hi")
        print(f"  SUCCESS! {m_name}")
    except Exception as e:
        print(f"  FAILED! {m_name}: {e}")
