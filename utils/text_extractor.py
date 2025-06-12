import os
import fitz # PyMuPDF
import docx
import chardet
import re

ALLOWED_EXTENSIONS = {'.pdf', '.txt', '.docx'}

def get_extension(file_path: str) -> str:
    return os.path.splitext(file_path)[1].lower()

def sanitize_text(text: str) -> str:
    """
    Prevents XSS by converting <script> to printable characters.

    Args:
        text (str): The input text to be summarized.
    
    Returns:
        str: The sanitized input text, free of injected <script> & non-printable characters.
    """
    cleaned = re.sub(r'[^\x20-\x7E\n\r\t]', '', text.strip())
    return ' '.join(cleaned.split())

def extract_text_from_txt(file_path: str) -> str:
    with open(file_path, 'rb') as f:
        raw_data = f.read()
        encoding = chardet.detect(raw_data)['encoding'] or 'utf-8'
    with open(file_path, 'r', encoding=encoding, errors='ignore') as f:
        return sanitize_text(f.read())

def extract_text_from_docx(file_path: str) -> str:
    doc = docx.Document(file_path)
    full_text = [para.text for para in doc.paragraphs]
    return sanitize_text('\n'.join(full_text))
    
def extract_text_from_pdf(file_path: str, start_page=1, end_page=None) -> str:
    doc = fitz.open(file_path)
    text = ''
    for page_index in range(doc.page_count):
        if not end_page: end_page = doc.page_count - 1
        if page_index >= start_page - 1 and page_index <= end_page:
            text += doc[page_index].get_text()
    return sanitize_text(text)

def extract_text(file_path: str, start_page=1, end_page=None) -> str:
    ext = get_extension(file_path)
    if ext not in ALLOWED_EXTENSIONS:
        raise ValueError(f"Unsupported file type: {ext}")
    
    if ext == '.txt':
        return extract_text_from_txt(file_path)
    elif ext == '.docx':
        return extract_text_from_docx(file_path)
    elif ext == '.pdf':
        return extract_text_from_pdf(file_path, start_page, end_page)