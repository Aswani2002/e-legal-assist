import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=key)

model_name = 'gemini-2.0-flash'
try:
    print(f"Testing {model_name}...")
    model = genai.GenerativeModel(model_name)
    response = model.generate_content("Hello, this is a test.")
    print(f"  SUCCESS! Response: {response.text[:50]}...")
except Exception as e:
    print(f"  FAILED! Error: {e}")
