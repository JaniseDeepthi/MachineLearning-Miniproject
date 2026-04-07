import docx2txt
from pdfminer.high_level import extract_text

def extract_resume_text(file_path):

    text = ""

    if file_path.endswith(".pdf"):
        text = extract_text(file_path)

    elif file_path.endswith(".docx"):
        text = docx2txt.process(file_path)

    return text.lower()