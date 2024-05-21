import os
import re
from pdfminer.high_level import extract_text
# Eae.

def extract_paragraphs_containing_keywords(pdf_path, keywords):
    text = extract_text(pdf_path)
    # Assuming paragraphs are separated by one new line
    paragraphs = text.split('\n')
    
    keyword_pattern = re.compile(r'\b(?:' + '|'.join(keywords) + r')\b', re.IGNORECASE)
    
    matched_paragraphs = [para for para in paragraphs if keyword_pattern.search(para)]
    
    return matched_paragraphs

def main(directory, keywords):
    keyword_list = keywords.split(',')
    results = {}
    
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(directory, filename)
            paragraphs = extract_paragraphs_containing_keywords(pdf_path, keyword_list)
            results[filename] = paragraphs
            
    return results

if __name__ == "__main__":
    # Select the directory where the PDF files are located (use \\ instead of \)
    directory = "C:\\Users\\User\\Desktop\\pdf_files"
    # Add keywords separated by commas
    keywords = "example, keyword, test"
    
    results = main(directory, keywords)
    
    for filename, paragraphs in results.items():
        print(f"File: {filename}")
        for paragraph in paragraphs:
            print(paragraph)
            print('-' * 80)