import pdfplumber
def extract_pdf(path):
    with pdfplumber.open(path) as pdf:
        all_text=""
        for page in pdf.pages:
            all_text+=page.extract_text() or ""
        return all_text
text=extract_pdf("samples/resume_simple.pdf")
print(text)