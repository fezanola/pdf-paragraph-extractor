import os
import PyPDF2
import pandas as pd
import json
import textwrap

# Função para extrair texto de um PDF
def extract_text_from_pdf(pdf_path):
    pdf_reader = PyPDF2.PdfReader(pdf_path)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

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

def process_pdfs_in_folder(folder_path, search_terms):
    results = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            text = extract_text_from_pdf(pdf_path)
            search_results = search_in_text(text, search_terms)
            results[filename] = search_results
    return results

def save_results(results, output_folder):
    # Salvar em CSV
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

    # Salvar em TXT
    with open(os.path.join(output_folder, 'search_results.txt'), 'w') as txt_file:
        for pdf_name, search_results in results.items():
            txt_file.write(f"Results for {pdf_name}:\n")
            for search_term, lines in search_results.items():
                txt_file.write(f"Search Term: {search_term}\n")
                for line in lines:
                    txt_file.write(f"{line}\n")
                txt_file.write("\n")

    # Salvar em JSON
    with open(os.path.join(output_folder, 'search_results.json'), 'w') as json_file:
        json.dump(results, json_file, indent=4)

def create_output_directory(output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

if __name__ == "__main__":
    # Caminho da pasta com PDFs (área de trabalho)
    folder_path = "C:\\Users\\victo\\OneDrive\\Área de Trabalho\\PDFs_scraper"

    # Termos de pesquisa (pode ser ajustado conforme necessário)
    search_terms = ["minimundo", "mundo real", "É uma macrodefinição ou descrição de alto nível"]

    # Processar PDFs e obter resultados
    results = process_pdfs_in_folder(folder_path, search_terms)

    # Diretório de saída para salvar os resultados (pasta do projeto)
    output_folder = os.path.dirname(os.path.abspath(__file__))
    create_output_directory(output_folder)

    # Salvar os resultados nos formatos CSV, TXT e JSON
    save_results(results, output_folder)

    print("Resultados salvos com sucesso em CSV, TXT e JSON.")

    # Imprimir resultados no PyCharm (Console)
    print("\nResultados no PyCharm:\n")
    for filename, search_results in results.items():
        print(f"File: {filename}")
        for search_term, lines in search_results.items():
            print(f"\n{search_term}:")
            for i, line in enumerate(lines):
                if i > 0:
                    print("-" * 140)  # Adiciona uma linha separadora entre as respostas
                wrapped_text = textwrap.fill(line, width=140)
                print(wrapped_text)
        print("\n")