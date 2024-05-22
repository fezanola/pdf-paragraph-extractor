# PDF Keyword Search Application
This application searches for keywords in PDF files, extracts relevant text, and saves the results in JSON, TXT, and CSV formats.

## Installation
Ensure you have the necessary libraries:

```bash
pip install PyPDF2 pandas
```

## Usage
### Folder Structure
```css
your_project/
├── main.py
├── pdf_utils.py
├── search_utils.py
└── file_utils.py
```

## Scripts Overview
`pdf_utils.py`:  
extract_text_from_pdf(pdf_path): Extracts text from a PDF file.  
`search_utils.py`:  
 search_in_text(text, search_terms): Searches for terms in text.  
`file_utils.py`:  
 `create_output_directory(output_folder)`: Ensures the output directory exists.  
 `save_results(results, output_folder)`: Saves results in CSV, TXT, and JSON formats.  
`main.py`  
 Prompts user for folder path, search terms, and output directory, then processes PDFs, searches terms, and saves results.


## Running the Application
1. Run main.py.  
2. Follow the prompts to enter the folder path, search terms, and output directory.  
3. Results will be saved in CSV, TXT, and JSON formats in the specified directory.  
