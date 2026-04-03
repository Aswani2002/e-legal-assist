import os
from app.utils import extract_text_from_document

test_file = "test_doc.txt"
if not os.path.exists(test_file):
    with open(test_file, 'w') as f:
        f.write("This is a test legal document about a contract.")

text = extract_text_from_document(test_file)
print(f"Extracted text: {text}")
