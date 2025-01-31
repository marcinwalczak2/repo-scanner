import json
import xml.etree.ElementTree as ET

def process_toc_file(input_file, name):
    """Extracts Title and .htm filename from TocEntry tags in an XML-like file."""
    entries = []

    # Read the file content
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Wrap content in a root tag to ensure it's valid XML
    xml_content = f"<root>{content}</root>"

    # Parse XML
    root = ET.fromstring(xml_content)

    # Process each TocEntry (case-insensitive handling)
    for toc_entry in root.iter('TocEntry'):
        title = toc_entry.get('Title', '').strip()

        # Extract only .htm filenames from the Link attribute
        link = toc_entry.get('Link', '')
        html_filename = link.split('/')[-1] if (link and link.endswith('.htm')) else ''

        if title and html_filename:  # Ensure only valid entries are added
            entries.append({
                'title': title,
                'filename': html_filename,
                'name': name
            })

    # Output filename
    output_file = f"toc_entries_{name}.json"

    # Save results to JSON
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(entries, f, indent=4)

    return output_file

# Example usage
if __name__ == "__main__":
    input_file = 'C:\\Code\\Repo Scan Test\\NameList\\toctags2.txt'  # Update with actual file path
    name = "michael"
    output_file = process_toc_file(input_file, name)
    print(f"JSON file created: {output_file}")