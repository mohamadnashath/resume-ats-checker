import pdfplumber
from docx import Document
def extract_pdf(path):
    with pdfplumber.open(path) as pdf:
        all_text=""
        for page in pdf.pages:
            all_text+=(page.extract_text() or "") +"\n"
        return all_text

def extract_docx(path):
    doc=Document(path)
    all_text=""
    for para in doc.paragraphs:
        all_text+=para.text +"\n"
    return all_text

if __name__=="__main__":
    print(extract_pdf("samples/resume_simple.pdf"))
    print(extract_docx("samples/resume_data_science.docx"))
    print(extract_pdf("samples/resume_table_layout.pdf"))
