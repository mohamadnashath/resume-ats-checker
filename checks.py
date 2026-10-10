import pdfplumber
import re
from docx import Document
def check_length(text):
    word_count=len(text.split())
    if word_count<75:
        return f"Resume is very short ({word_count} words). Add more detail about your experience and projects."
    else:
        return None
SECTIONS = {
    "experience": ["experience", "work experience", "work history", "employment", "work", "internship"],
    "education": ["education", "academic"],
    "skills": ["skills", "technical skills"],
}

def check_sections(text):
    lines = [line.strip().lower() for line in text.splitlines()]
    missing = []
    for section, names in SECTIONS.items():
        found = any(re.match(re.escape(name) + r"\b", line) for line in lines for name in names)
        if not found:
            missing.append(section)
    return missing
def check_tables(path):
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            if page.find_tables():
                return "Your resume contains a table, which many ATS systems can't parse correctly"
        return None
def check_tables_docx(path):
    doc=Document(path)
    if doc.tables:
        return "Your resume contains a table, which many ATS systems can't parse correctly"
    return None



if __name__ == "__main__":
    from extract import extract_pdf,extract_docx
    print(check_length(extract_pdf("samples/resume_table_layout.pdf")))
    print(check_length(extract_pdf("samples/resume_simple.pdf")))
    print(check_length(extract_docx("samples/resume_data_science.docx")))
    print(check_sections(extract_pdf("samples/resume_simple.pdf")))
    print(check_sections(extract_docx("samples/resume_data_science.docx")))
    print(check_sections(extract_pdf("samples/resume_table_layout.pdf")))
    print(check_tables("samples/resume_table_layout.pdf"))
    print(check_tables("samples/resume_simple.pdf"))
    print(check_tables_docx("samples/resume_data_science.docx"))