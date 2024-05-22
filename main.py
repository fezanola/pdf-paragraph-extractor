import os
import textwrap

from typing import List, Dict
from pdf_utils import extract_text_from_pdf
from search_utils import search_in_text
from file_utils import save_results, create_output_directory

# Main Function to Process all PDFs in the Folder
def process_pdfs_in_folder(folder_path: str, search_terms: List[str]) -> Dict[str, Dict[str, List[str]]]:
    results = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            text = extract_text_from_pdf(pdf_path)
            search_results = search_in_text(text, search_terms)
            results[filename] = search_results
    return results

# Script Execution
if __name__ == "__main__":
    # Path to the folder containing PDFs
    folder_search = input("Enter the path to the folder containing the PDFs: ").strip()

    # Search terms
    search_info = input("Enter the search terms, separated by commas: ").split(',')

    # Process PDFs and get results
    result = process_pdfs_in_folder(folder_search.strip(), [term.strip() for term in search_info])

    # Output directory to save the results
    result_folder = input("Enter the path to the folder where you want to save the results: ").strip()

    # Ensure the output directory exists
    create_output_directory(result_folder)

    # Save the results in CSV, TXT and JSON formats
    save_results(result, result_folder)

    print("Results saved successfully in CSV, TXT and JSON.")

    # Print results
    print("Results:\n")
    for file_name, search_result in result.items():
        print(f"File: {file_name}")
        for search_item, lines in search_result.items():
            print(f"\n{search_item}:")
            for i, line in enumerate(lines):
                if i > 0:
                    print("\n" + "-" * 140 + "\n")  # Adds a separator line between the answers
                wrapped_text = textwrap.fill(line, width=140)
                print(wrapped_text)
        print("\n")
