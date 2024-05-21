# INTRODUCTION
This application performs a keyword search on a set of PDF files.

It extracts the text from the PDFs, identifies the paragraphs containing the keywords and displays the results on the screen, as well as offering options to save the results to a JSON file and create a CSV index of the keywords found.

## 📚 Section 1: Library Installation

This initial section prepares the environment for application execution by installing the necessary libraries.

*   `!pip install PyPDF2:` This line installs the PyPDF2 library in the Google Colab environment.
*   `!pip install pandas:` This line installs the pandas library in the Google Colab environment.
*   `import os:` Allows interaction with the operating system, such as accessing files and directories.
*   `import pandas as pd:` Facilitates referencing pandas functions and classes in our code.
*   `import PyPDF2:` Provides functions for extracting text from PDF files.
*   `import textwrap:` Enables formatting of output text, wrapping long lines to improve readability.
*   `import json:` Allows working with JSON files, which are text files that store data in a structured format.


## 📂 Section 2: Google Drive Connection:

This section explains the objective of connecting the code to Google Drive to access PDF files.
*   `google.colab import drive:` Enables connecting to Google Drive in the Google Colab environment.
*   `drive.mount('/content/drive'):` This code line mounts Google Drive in the Google Colab environment.

This allows the script to access Google Drive files as if they were in Colab's own file system.


## 📖 Section 3: Function to Extract Text from a PDF

This section defines the `extract_text_from_pdf` function, responsible for reading the textual content of a PDF file and returning the extracted text.

**Explanation:**

1. **Reading the PDF:**
   - `pdf_reader = PyPDF2.PdfReader(pdf_path)`: The `PdfReader` function from the PyPDF2 library is used to open the PDF file specified by the `pdf_path`. The `pdf_reader` object represents the opened PDF.

2. **Iterating through Pages:**
   - `for page in pdf_reader.pages:`: A `for` loop is used to iterate over each page of the PDF.

3. **Extracting Text:**
   - `text += page.extract_text()`: The `extract_text` function of the `page` object is called to extract the text from each page. The extracted text is concatenated to the `text` variable.

4. **Returning Text:**
   - `return text`: The function returns the text extracted from all pages of the PDF.

**In summary:** The `extract_text_from_pdf` function receives the path of a PDF file as input, opens the file, iterates through each page, extracts the text from each page, concatenates the text into a single string, and returns it as the result.



## 🔍 Section 4: Function to Search for Words or Phrases in the Extracted PDF Text

This section defines the `search_in_text` function, responsible for searching for the provided search terms within the text extracted from the PDF and returning a list of lines containing the terms.

**Explanation:**

1. **Initializing the Results Dictionary:**
   - `results = {}`: Creates an empty dictionary called `results`, which will be used to store the search results. The dictionary keys will be the search terms, and the values will be lists of lines containing those terms.

2. **Separating Text into Lines:**
   - `lines = text.split('\n')`: The text extracted from the PDF is split into a list of lines using the `\n` character (newline) as a delimiter.

3. **Searching for Terms:**
   - `for line in lines:`: A `for` loop iterates over each line of the text.
   - `for term in search_terms:`: Another `for` loop iterates over each search term in the `search_terms` list.
   - `if term.lower() in line.lower()`: The `lower` function is used to convert the search term and the line to lowercase, ensuring that the search is case-insensitive. If the term is found in the line, the code enters the `if` block.

4. **Storing the Results:**
   - `if term in results:`: Checks if the search term already exists as a key in the `results` dictionary. If it exists, it means that lines with this term have already been found, so the current line is added to the list of lines corresponding to the term.
   - `else:`: If the term does not yet exist as a key in the `results` dictionary, it means that this is the first line found with this term, so a new list is created for the term and the current line is added to that list.
   - `results[term].append(line.strip())`: The current line is added to the list of lines corresponding to the term.


## 📂 Section 5: Main Function to Process all PDFs in the Folder

This section defines the `process_pdfs_in_folder` function, responsible for iterating through all PDF files in a specific folder, extracting the text from each one, performing the search for terms, and storing the results.

**Explanation:**

1. **Initializing the Results Dictionary:**
   - `results = {}`: Creates an empty dictionary called `results`, which will be used to store the search results for each PDF. The dictionary keys will be the names of the PDF files, and the values will be dictionaries containing the search terms and the corresponding lines in each PDF.

2. **Iterating through PDF Files:**
   - `for filename in os.listdir(folder_path):`: A `for` loop iterates over all files in the folder specified by the `folder_path`.
   - `if filename.endswith(".pdf"):`: Checks if the file name ends with ".pdf". If not, the file is not a PDF and is ignored.

3. **Text Extraction and Search:**
   - `pdf_path = os.path.join(folder_path, filename)`: Creates the full path to the PDF file, combining the folder path and the file name.
   - `text = extract_text_from_pdf(pdf_path)`: Calls the `extract_text_from_pdf` function to extract the text from the PDF.
   - `search_results = search_in_text(text, search_terms)`: Calls the `search_in_text` function to search for the search terms in the extracted text.

4. **Storing the Results:**
   - `results[filename] = search_results`: Stores the search results for the current file (file name as key) in the `results` dictionary.

5. **Returning the Results:**
   - `return results`: The function returns the `results` dictionary, which contains the search results for all PDF files in the folder.

**In summary:** The `process_pdfs_in_folder` function receives the path of a folder and the list of search terms as input. It iterates through all PDF files in the folder, extracts the text from each one, searches for the search terms, and stores the results in a dictionary. The dictionary with the results for each PDF is returned as the result.



## 💾 Section 6: Function to Save Results in Different Formats

This section defines the `save_results` function, responsible for saving the search results in different formats, such as CSV, TXT, and JSON.

**Explanation:**

1. **Saving to CSV:**
   - `csv_rows = []`: Creates an empty list called `csv_rows`, which will be used to store the data for the CSV file.
   - `for pdf_name, search_results in results.items():`: A `for` loop iterates over each entry in the `results` dictionary. Each entry represents a PDF (PDF name as key) and the search results in that PDF (dictionary with terms and corresponding lines as value).
   - `for search_term, lines in search_results.items():`: Another `for` loop iterates over each search term and the corresponding lines in the results dictionary of the current PDF.
   - `for line in lines:`: A third `for` loop iterates over each line containing the current search term.
   - `csv_rows.append({'pdf_name': pdf_name, 'line_text': line, 'search_term': search_term})`: Creates a dictionary with the relevant information (PDF name, line text, and search term) and adds this dictionary to the `csv_rows` list.
   - `df = pd.DataFrame(csv_rows)`: Creates a Pandas DataFrame from the `csv_rows` list.
   - `df.to_csv(os.path.join(output_folder, 'search_results.csv'), index=False)`: Saves the Pandas DataFrame as a CSV file at the specified path, without including the DataFrame index.

2. **Saving to TXT:**
   - `with open(os.path.join(output_folder, 'search_results.txt'), 'w') as txt_file:`: Opens a TXT file for writing at the specified path.
   - `for pdf_name, search_results in results.items():`: A `for` loop iterates over each PDF and the search results.
   - `txt_file.write(f"Results for {pdf_name}:\n")`: Writes the PDF name to the TXT file.
   - `for search_term, lines in search_results.items():`: A `for` loop iterates over each search term and the corresponding lines.
   - `txt_file.write(f"Search Term: {search_term}\n")`: Writes the search term to the TXT file.
   - `for line in lines:`: A `for` loop iterates over each line containing the search term.
   - `txt_file.write(f"{line}\n")`: Writes the line to the TXT file.
   - `txt_file.write("\n")`: Inserts a blank line in the TXT file after each search term.

3. **Saving to JSON:**
   - `with open(os.path.join(output_folder, 'search_results.json'), 'w') as json_file:`: Opens a JSON file for writing at the specified path.
   - `json.dump(results, json_file, indent=4)`: Uses the `json.dump` function to serialize the `results` dictionary into JSON format and write it to the file. The `indent=4` argument sets the indentation to improve the readability of the JSON file.

**In summary:** The `save_results` function receives the search results and the output folder path as input. It saves the results in three different formats: CSV, TXT, and JSON. The CSV format is created using a Pandas DataFrame, the TXT format is created using file writing operations, and the JSON format is created using the `json.dump` function.



## 📁 Section 7: Function to Create Output Directory if it Doesn't Exist

This section defines the `create_output_directory` function, responsible for checking if the output folder already exists. If it doesn't exist, the function creates the folder.

**Explanation:**

1. **Checking Folder Existence:**
   - `if not os.path.exists(output_folder):`: Checks if the folder specified by the `output_folder` path exists. If the folder doesn't exist, the code enters the `if` block.

2. **Creating the Folder:**
   - `os.makedirs(output_folder)`: The `makedirs` function from the `os` module is used to create the folder specified by the `output_folder` path, including parent folders if necessary.

**In summary:** The `create_output_directory` function checks if the output folder exists. If it doesn't exist, the function creates the folder before saving the results. This ensures that the output files are saved in the correct folder, even if it doesn't exist previously.



## 🚀 Section 8: Script Execution

This section contains the code that is executed when the script is started. This is where the application is configured, and the results are generated and displayed.

**Explanation:**

1. **Connecting to Google Drive:**
   - `from google.colab import drive`: Imports the `drive` module from Google Colab to allow access to Google Drive.
   - `drive.mount('/content/drive')`: Mounts Google Drive in the Google Colab environment, allowing the script to access Google Drive files.

2. **Defining the Folder Path and Search Terms:**
   - `folder_path = '/content/drive/MyDrive/PDFs_scraper'`: Defines the path of the folder containing the PDF files.
   - `search_terms = ["minimundo", "mundo real", "É uma macrodefinição ou descrição de alto nível"]`: Defines the list of search terms that will be used.

3. **Processing PDFs and Obtaining Results:**
   - `results = process_pdfs_in_folder(folder_path, search_terms)`: Calls the `process_pdfs_in_folder` function to process the PDFs in the specified folder and obtain the search results.

4. **Creating the Output Directory:**
   - `output_folder = '/content'`: Defines the path of the folder where the results will be saved.
   - `create_output_directory(output_folder)`: Calls the `create_output_directory` function to ensure that the output folder exists.

5. **Saving the Results:**
   - `save_results(results, output_folder)`: Calls the `save_results` function to save the results in different formats (CSV, TXT, JSON).

6. **Displaying the Results in Colab:**
   - `print("Resultados salvos com sucesso em CSV, TXT e JSON.")`: Prints a message on the Colab screen informing that the results have been saved.
   - `for filename, search_results in results.items():`: A `for` loop iterates over each PDF and the search results.
   - `print(f"\n{search_term}:")`: Prints the search term on the Colab screen.
   - `for i, line in enumerate(lines):`: A `for` loop iterates over each line containing the search term.
   - `print("-" * 140)`: Prints a separating line between different responses.
   - `wrapped_text = textwrap.fill(line, width=140)`: Applies "text wrap" to the line to improve readability.
   - `print(wrapped_text)`: Prints the line with the "text wrap" applied to the Colab screen.

**In summary:** Section 8 is responsible for executing the script, connecting to Google Drive, processing the PDFs, saving the results in different formats, and displaying the results on the Colab screen.
