import json

# Load LIST1 and LIST2 from their respective files
with open('C:\\Code\\Repo Scan Test\\scan_results_20250131_012857.json', 'r') as f1:
    list1 = json.load(f1)

with open('C:\\Code\\Repo Scan Test\\NameList\\NameJson\\combined_toc_entries.json', 'r') as f2:
    list2 = json.load(f2)

# Initialize the result dictionary
list3 = {}

# Process each entry in LIST2
for entry in list2:
    filename = entry['filename']
    name = entry['name']
    title = entry['title']
    
    # Check if the current filename exists in LIST1's findings
    if filename in list1['findings']:
        # Extract the findings for this file
        findings = list1['findings'][filename]
        
        # Create the file entry with title and findings
        file_entry = {
            'title': title,
            'filename': filename,
            'findings': findings
        }
        
        # Add to the team member's entry in list3
        if name not in list3:
            list3[name] = []
        list3[name].append(file_entry)

# Write the result to LIST3.json
with open('LIST3.json', 'w') as f3:
    json.dump(list3, f3, indent=4)