import json

# Load the first JSON file (json1)
with open('json1.json', 'r') as f1:
    json1_data = json.load(f1)

# Load the second JSON file (json2)
with open('json2.json', 'r') as f2:
    json2_data = json.load(f2)

# Create a mapping from filename to title and name from json2
filename_to_info = {item['filename']: {'title': item['title'], 'name': item['name']} for item in json2_data}

# Prepare the merged list of files
merged_files = []
for file_entry in json1_data['files']:
    html_filename = file_entry['html_file']
    if html_filename in filename_to_info:
        # Create a new entry with updated title and name
        merged_entry = file_entry.copy()
        merged_entry['title'] = filename_to_info[html_filename]['title']
        merged_entry['name'] = filename_to_info[html_filename]['name']
        merged_files.append(merged_entry)

# Construct the merged JSON structure
merged_output = {"files": merged_files}

# Write the merged result to a new JSON file
with open('merged_output.json', 'w') as out_file:
    json.dump(merged_output, out_file, indent=4)