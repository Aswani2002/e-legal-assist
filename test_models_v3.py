import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

key = os.getenv('GOOGLE_API_KEY')
print(f"Testing Key: ...{key[-4:]}")

genai.configure(api_key=key)

models_to_test = [
    'gemini-1.5-flash',
    'gemini-2.0-flash',
    'gemini-flash-latest',
    'gemini-pro-latest',
]

for model_name in models_to_test:
    try:
        print(f"Testing {model_name}...")
        model = genai.GenerativeModel(model_name)
        response = model.generate_content("Hello, this is a test.")
        print(f"  SUCCESS! Response: {response.text[:50]}...")
    except Exception as e:
        print(f"  FAILED! Error: {e}")

print("\nListing all supported models for generateContent:")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"  - {m.name}")
except Exception as e:
    print(f"Error listing models: {e}")
