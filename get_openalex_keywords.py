import requests
from tqdm import tqdm
import re

def extract_doi(text):
    # Regex to find DOI pattern
    match = re.search(r'(10\.\d{4,9}/[-._;()/:A-Z0-9]+)', text, re.IGNORECASE)
    return match.group(1) if match else None

# Load and clean DOIs
with open('dois.txt', 'r') as f:
    raw_lines = [line.strip() for line in f if line.strip()]

# Extract valid DOIs only
dois = []
for line in raw_lines:
    doi = extract_doi(line)
    if doi:
        dois.append(doi)
    else:
        print(f"⚠️ Skipped (not a DOI): {line}")

print(f"\n✅ Found {len(dois)} valid DOIs. Starting metadata fetch...")

ris_entries = []

for doi in tqdm(dois):
    openalex_id = f"https://openalex.org/doi/{doi}"
    url = f"https://api.openalex.org/works/{openalex_id}"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        title = data.get('title', 'No Title')
        concepts = data.get('concepts', [])
        keywords = [concept['display_name'] for concept in concepts]

        # RIS entry
        ris = []
        ris.append("TY  - JOUR")
        ris.append(f"TI  - {title}")
        ris.append(f"DO  - {doi}")
        for kw in keywords:
            ris.append(f"KW  - {kw}")
        ris.append("ER  - \n")

        ris_entries.append('\n'.join(ris))

    except Exception as e:
        print(f"❌ Error fetching DOI {doi}: {e}")

# Save RIS
with open("openalex_keywords.ris", "w", encoding="utf-8") as f:
    f.write('\n'.join(ris_entries))

print("\n🎉 Done! File saved as 'openalex_keywords.ris'.")
