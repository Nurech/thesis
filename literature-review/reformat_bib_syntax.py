import bibtexparser

def format_bib_entry(entry):
    formatted_entry = {}
    for key, value in entry.items():
        formatted_key = key.lower()
        formatted_value = value.strip()
        formatted_entry[formatted_key] = formatted_value
    return formatted_entry

def process_bib_file(input_file, output_file):
    with open(input_file, 'r') as bib_file:
        bib_data = bibtexparser.load(bib_file)

    formatted_entries = []
    for entry in bib_data.entries:
        formatted_entry = format_bib_entry(entry)
        formatted_entries.append(formatted_entry)

    bib_data.entries = formatted_entries

    with open(output_file, 'w') as bib_file:
        bibtexparser.dump(bib_data, bib_file)

input_file = 'ref.bib'
output_file = 'ref_formatted.bib'
process_bib_file(input_file, output_file)
