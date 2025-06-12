from utils.text_extractor import extract_text
import os

file_path = os.path.join(os.getcwd(), 'docs/test_data.txt')

try:
    text = extract_text(file_path)
    print(f"Extracted text: {text[:1000]}")
except Exception as e:
    print()