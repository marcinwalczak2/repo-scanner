import json
import re
from xml.etree import ElementTree as ET

def process_toc_file(input_file, name):
    # List to store all entries
    entries = []
    
    # Read the file content
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Wrap the content in a root element to make it valid XML
    xml_content = f"<root>{content}</root>"
    
    # Parse the XML
    root = ET.fromstring(xml_content)
    
    # Process each TocEntry
    for toc_entry in root.findall('TocEntry'):
        # Get the title
        title = toc_entry.get('Title')
        
        # Get the link and extract just the HTML filename
        link = toc_entry.get('Link')
        html_filename = link.split('/')[-1] if link else ''
        
        # Create entry dictionary
        entry = {
            'title': title,
            'filename': html_filename,
            'name': name
        }
        
        entries.append(entry)
    
    # Create output filename using the name variable
    output_file = f"toc_entries_{name}.json"
    
    # Write to JSON file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(entries, f, indent=4)
    
    return output_file

# Example usage
if __name__ == "__main__":
    input_file = 'C:\\Code\\Repo Scan Test\\NameList\\toctags2.txt' # Your input file name
    name = "michael"  # Your name variable
    output_file = process_toc_file(input_file, name)
    print(f"JSON file created: {output_file}")