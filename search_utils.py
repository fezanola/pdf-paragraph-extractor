from typing import List, Dict

# Function to Search for Words or Phrases in the Extracted PDF Text
def search_in_text(text: str, search_terms: List[str]) -> Dict[str, List[str]]:
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