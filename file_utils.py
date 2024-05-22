import os
import pandas as pd
import json
from typing import List, Dict

# Function to Create Output Directory if it Doesn't Exist
def create_output_directory(output_folder: str):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

# Function to Save Results in Different Formats
def save_results(results: Dict[str, Dict[str, List[str]]], output_folder: str):
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
