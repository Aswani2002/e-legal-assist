import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

keys = [
    os.getenv('GOOGLE_API_KEY'),
    os.getenv('GOOGLE_API_KEY_1'),
    os.getenv('GOOGLE_API_KEY_2'),
    os.getenv('GOOGLE_API_KEY_3'),
    os.getenv('GOOGLE_API_KEY_4'),
    os.getenv('GOOGLE_API_KEY_5'),
]

# Filter out empty keys and remove duplicates
active_keys = list(set([k for k in keys if k]))

print(f"Found {len(active_keys)} unique keys.")

for idx, key in enumerate(active_keys):
    try:
        print(f"Testing Key {idx+1} (ends in ...{key[-4:]}):")
        genai.configure(api_key=key)
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f"  Available: {m.name}")
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content("hello")
        print(f"  Result: Success! Response: {response.text[:20]}...")
    except Exception as e:
        print(f"  Result: FAILED! Error: {str(e)[:100]}")
