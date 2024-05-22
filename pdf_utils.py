import PyPDF2

# Function to Extract Text from a .PDF file
def extract_text_from_pdf(pdf_path: str) -> str:
    pdf_reader = PyPDF2.PdfReader(pdf_path)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text