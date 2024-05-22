# Section 1: Library Installation
import os
import PyPDF2
import pandas as pd
import json
import textwrap


# Section 2: Function to Extract Text from a PDF
def extract_text_from_pdf(pdf_path):
    pdf_reader = PyPDF2.PdfReader(pdf_path)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text


# Section 3: Function to Search for Words or Phrases in the Extracted PDF Text
def search_in_text(text, search_terms):
    results = {}
    lines = text.split('\n')
    for line in lines:
        for term in search_terms:
            if term.lower() in line.lower():
                if term in results:
                    results[term].append(line.strip())
                else:
                    results[term] = [line.strip()]
    return results


# Section 4: Main Function to Process all PDFs in the Folder
def process_pdfs_in_folder(folder_path, search_terms):
    results = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            text = extract_text_from_pdf(pdf_path)
            search_results = search_in_text(text, search_terms)
            results[filename] = search_results
    return results


# Section 5: Function to Save Results in Different Formats
def save_results(results, output_folder):
    # Save to CSV
    csv_rows = []
    for pdf_name, search_results in results.items():
        for search_term, lines in search_results.items():
            for line in lines:
                csv_rows.append({
                    'pdf_name': pdf_name,
                    'line_text': line,
                    'search_term': search_term
                })
    df = pd.DataFrame(csv_rows)
    df.to_csv(os.path.join(output_folder, 'search_results.csv'), index=False)

    # Save to TXT
    with open(os.path.join(output_folder, 'search_results.txt'), 'w') as txt_file:
        for pdf_name, search_results in results.items():
            txt_file.write(f"Results for {pdf_name}:\n")
            for search_term, lines in search_results.items():
                txt_file.write(f"Search Term: {search_term}\n")
                for line in lines:
                    txt_file.write(f"{line}\n")
                txt_file.write("\n")

        # Save to JSON
        with open(os.path.join(output_folder, 'search_results.json'), 'w', encoding='utf-8') as json_file:
            json.dump(results, json_file, indent=4, ensure_ascii=False)


# Section 6: Function to Create Output Directory if it Doesn't Exist
def create_output_directory(output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)


# Section 8: Script Execution
if __name__ == "__main__":
    # Path to the folder containing PDFs (desktop)
    folder_search = "C:\\Users\\[user_name]\\desktop\\[folder_name]"

    # Search terms (can be adjusted as needed)
    search_info = ["[word1]", "[word2]", "[phrase1]"]

    # Process PDFs and get results
    result = process_pdfs_in_folder(folder_search, search_info)

    # Output directory to save the results (project folder)
    result_folder = os.path.dirname(os.path.abspath(__file__))
    create_output_directory(result_folder)

    # Save the results in CSV, TXT and JSON formats
    save_results(result, result_folder)

    print("Results saved successfully in CSV, TXT and JSON.")

    # Print results in PyCharm (Console)
    print("\nResults in PyCharm:\n")
    for file_name, search_result in result.items():
        print(f"File: {file_name}")
        for search_item, dash in search_result.items():
            print(f"\n{search_item}:")
            for i, row in enumerate(dash):
                if i > 0:
                    print("-" * 140)  # Adds a separator line between the answers
                wrapped_text = textwrap.fill(row, width=140)
                print(wrapped_text)
        print("\n")
