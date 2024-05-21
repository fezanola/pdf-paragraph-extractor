# INTRODUCTION
This application performs a keyword search on a set of PDF files.

It extracts the text from the PDFs, identifies the paragraphs containing the keywords and displays the results on the screen, as well as offering options to save the results to a JSON file and create a CSV index of the keywords found.


## 📚 Section 1: Library Installation

This initial section prepares the environment for application execution by installing the necessary libraries.

*   `!pip install PyPDF2:` This line installs the PyPDF2 library in the Computer environment.
*   `!pip install pandas:` This line installs the pandas library in the Computer environment.
*   `import os:` Allows interaction with the operating system, such as accessing files and directories.
*   `import PyPDF2:` Provides functions for extracting text from PDF files.
*   `import pandas as pd:` Facilitates referencing pandas functions and classes in our code.
*   `import json:` Allows working with JSON files, which are text files that store data in a structured format.
*   `import textwrap:` Enables formatting of output text, wrapping long lines to improve readability.


## 📖 Section 2: Function to Extract Text from a PDF

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


## 🔍 Section 3: Function to Search for Words or Phrases in the Extracted PDF Text

This section defines the `search_in_text` function which searches for specific words or phrases within the extracted text from a PDF file.

**Explanation:**

1. **Initialization:**
    - `results = {}`: Creates an empty dictionary to store the search results. Each key in this dictionary will be a search term, and the value will be a list of lines containing that term.
    - `lines = text.split('\n')`: Splits the extracted text into a list of lines using the newline character (`\n`) as a delimiter. This allows for easier searching within each line.

2. **Iterating through Lines:**
    - `for line in lines:`: This loop iterates over each line of the extracted text.

3. **Searching for Terms:**
    - `for term in search_terms:`: This nested loop iterates over each search term provided by the user.
    - `if term.lower() in line.lower()`: This condition checks if the search term (converted to lowercase) is present within the current line (also converted to lowercase). This ensures case-insensitive search.
    - `if term in results:`: Checks if the current term already exists as a key in the `results` dictionary.
    - `results[term].append(line.strip())`: If the term exists, the current line is appended to the list associated with that term in the dictionary.
    - `else:`: If the term doesn't exist as a key yet.
    - `results[term] = [line.strip()]`: Creates a new key in the `results` dictionary for the term and adds the current line as the first element of the list associated with it.

4. **Returning Results:**
    - `return results`: Returns the `results` dictionary, which contains the search results for each term.

**In summary:** The `search_in_text` function takes the extracted text from a PDF file and a list of search terms as input. It then iterates through each line of the text and checks for the presence of each search term. If a term is found in a line, it adds that line to the corresponding list in the `results` dictionary. Finally, it returns the `results` dictionary.


## 📂 Section 4: Main Function to Process all PDFs in the Folder

This section defines the `process_pdfs_in_folder` function, which processes all PDF files within a specified folder and performs search operations on their contents.

**Explanation:**

1. **Initialization:**
    - `results = {}`: Creates an empty dictionary to store the search results for each PDF file. The keys of this dictionary will be the PDF filenames, and the values will be the `results` dictionaries returned by the `search_in_text` function.

2. **Iterating through Files:**
    - `for filename in os.listdir(folder_path)`: This loop iterates over all files within the specified folder path.
    - `if filename.endswith(".pdf")`: Checks if the current filename ends with the `.pdf` extension, indicating a PDF file.

3. **Processing PDF Files:**
    - `pdf_path = os.path.join(folder_path, filename)`: Constructs the full path to the PDF file using the folder path and filename.
    - `text = extract_text_from_pdf(pdf_path)`: Calls the `extract_text_from_pdf` function to extract text from the current PDF file.
    - `search_results = search_in_text(text, search_terms)`: Calls the `search_in_text` function to search for the specified terms within the extracted text.
    - `results[filename] = search_results`: Adds the search results for the current PDF file (stored in the `search_results` dictionary) to the `results` dictionary, using the filename as the key.

4. **Returning Results:**
    - `return results`: Returns the `results` dictionary, which contains the search results for each PDF file in the folder.

**In summary:** The `process_pdfs_in_folder` function takes the path to a folder containing PDF files and a list of search terms as input. It then iterates over each PDF file in the folder, extracts its text, searches for the terms in the text, stores the search results in a dictionary using the filename as the key, and finally returns the dictionary containing the search results for all processed PDF files.


## 💾 Section 5: Function to Save Results in Different Formats

This section defines the `save_results` function, responsible for saving the search results in various formats (CSV, TXT, and JSON).

**Explanation:**

1. **Saving to CSV:**
    - `csv_rows = []`: Creates an empty list to store the data that will be written to the CSV file.
    - `for pdf_name, search_results in results.items()`: This loop iterates over each PDF file and its corresponding search results in the `results` dictionary.
    - `for search_term, lines in search_results.items()`: This nested loop iterates over each search term and its corresponding lines in the `search_results` dictionary.
    - `for line in lines`: This further nested loop iterates over each line that contains a match for the search term.
    - `csv_rows.append({'pdf_name': pdf_name, 'line_text': line, 'search_term': search_term})`: Creates a dictionary containing the PDF filename, the matched line of text, and the corresponding search term. This dictionary is then appended to the `csv_rows` list.
    - `df = pd.DataFrame(csv_rows)`: Creates a Pandas DataFrame from the data stored in the `csv_rows` list.
    - `df.to_csv(os.path.join(output_folder, 'search_results.csv'), index=False)`: Saves the DataFrame as a CSV file named `search_results.csv` in the specified `output_folder`. The `index=False` argument prevents the DataFrame's index from being saved in the CSV file.

2. **Saving to TXT:**
    - `with open(os.path.join(output_folder, 'search_results.txt'), 'w') as txt_file`: Opens a file named `search_results.txt` in write mode (`'w'`) within the `output_folder`. The `with` statement ensures the file is properly closed even if an error occurs.
    - `for pdf_name, search_results in results.items()`: Iterates over the PDF filenames and their corresponding search results.
    - `txt_file.write(f"Results for {pdf_name}:\n")`: Writes a heading indicating the PDF filename to the file.
    - `for search_term, lines in search_results.items()`: Iterates over search terms and their matching lines.
    - `txt_file.write(f"Search Term: {search_term}\n")`: Writes the search term to the file.
    - `for line in lines`: Iterates over each line that matches the search term.
    - `txt_file.write(f"{line}\n")`: Writes each matching line to the file.
    - `txt_file.write("\n")`: Adds an empty line to separate results from different search terms.

3. **Saving to JSON:**
    - `with open(os.path.join(output_folder, 'search_results.json'), 'w', encoding='utf-8') as json_file`: Opens a file named `search_results.json` in write mode (`'w'`) within the `output_folder`. The `encoding='utf-8'` argument ensures that the file can handle various characters, including Unicode characters.
    - `json.dump(results, json_file, indent=4, ensure_ascii=False)`: Dumps the `results` dictionary to the JSON file. The `indent=4` argument makes the JSON output more readable by indenting it. The `ensure_ascii=False` argument prevents non-ASCII characters from being escaped in the output.

**In summary:** The `save_results` function takes the search results dictionary and the output folder path as input. It then saves the results in three different formats: CSV, TXT, and JSON. The CSV format provides a tabular representation of the results, the TXT format provides a plain text representation, and the JSON format provides a structured representation of the results that can be easily parsed and used by other applications.


## 📁 Section 6: Function to Create Output Directory if it Doesn't Exist

This section defines the `create_output_directory` function which ensures that the specified output directory exists before saving the results.

**Explanation:**

1. **Checking for Directory Existence:**
    - `if not os.path.exists(output_folder):`: This condition checks if the specified output folder exists. If it doesn't exist, it will create the folder.
2. **Creating Directory:**
    - `os.makedirs(output_folder)`: Uses the `makedirs` function from the `os` library to create the specified output folder. If the folder already exists, this function will not create it again.

**In summary:** The `create_output_directory` function takes the output folder path as input. If the folder does not exist, it creates the folder to ensure that the results can be saved to the specified location.


## 🚀 Section 7: Script Execution

This section defines the main execution block of the script.

**Explanation:**

1. **Setting Folder Path and Search Terms:**
    - `folder_search = "C:\\Users\\[user_name]\\desktop\\[folder_name]"`: This line defines the path to the folder containing PDF files. This path should be replaced with the actual folder path on your computer.
    - `search_info = ["[word1]", "[word2]", "[phrase1]"]`: This line defines a list of words and phrases to be searched within the PDF files. You should replace this list with your desired search terms.

2. **Processing PDFs and Obtaining Results:**
    - `result = process_pdfs_in_folder(folder_search, search_info)`: Calls the `process_pdfs_in_folder` function to process all PDF files in the specified folder and search for the defined terms. The results are stored in the `result` variable.

3. **Creating Output Directory:**
    - `result_folder = os.path.dirname(os.path.abspath(__file__))`: Retrieves the directory path of the current script file.
    - `create_output_directory(result_folder)`: Calls the `create_output_directory` function to ensure the output directory exists.

4. **Saving Results:**
    - `save_results(result, result_folder)`: Calls the `save_results` function to save the search results in CSV, TXT, and JSON formats in the specified output directory.

5. **Printing Confirmation Message:**
    - `print("Results saved successfully in CSV, TXT and JSON.")`: Prints a message confirming that the results have been saved.

6. **Printing Results in PyCharm Console:**
    - `print("\nResults in PyCharm:\n")`: Prints a heading to separate the console output from previous output.
    - `for file_name, search_result in result.items()`: Iterates over the PDF filenames and their corresponding search results in the `result` dictionary.
    - `print(f"File: {file_name}")`: Prints the PDF filename.
    - `for search_item, dash in search_result.items()`: Iterates over the search terms and their matching lines in the `search_result` dictionary.
    - `print(f"\n{search_item}:")`: Prints the search term.
    - `for i, row in enumerate(dash)`: Iterates over each matching line for the search term.
    - `if i > 0:`: Adds a separator line between the answers if it is not the first answer.
    - `wrapped_text = textwrap.fill(row, width=140)`: Wraps the text of each line to a maximum width of 140 characters for better readability.
    - `print(wrapped_text)`: Prints the wrapped text to the console.
    - `print("\n")`: Adds an empty line to separate the results for different PDF files.

**In summary:** This section executes the main logic of the script. It defines the folder path, search terms, and output directory, calls the necessary functions to process PDF files and save the results, and displays the results in the PyCharm console. This section ties together all the previous sections and completes the workflow of the script.
