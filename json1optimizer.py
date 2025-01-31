import json

# Load JSON files with explicit UTF-8 encoding
with open('json1.json', 'r', encoding='utf-8') as f1:
    json1_data = json.load(f1)

with open('json2.json', 'r', encoding='utf-8') as f2:
    json2_data = json.load(f2)

# Create a filename-to-info mapping from json2
filename_to_info = {item['filename']: {'title': item['title'], 'name': item['name']} for item in json2_data}

# Merge data from json2 into json1
merged_files = []
for file_entry in json1_data['files']:
    html_filename = file_entry['html_file']
    if html_filename in filename_to_info:
        merged_entry = file_entry.copy()
        merged_entry['title'] = filename_to_info[html_filename]['title']
        merged_entry['name'] = filename_to_info[html_filename]['name']
        merged_files.append(merged_entry)

# Save the merged output with UTF-8 encoding
with open('merged_output.json', 'w', encoding='utf-8') as out_file:
    json.dump({"files": merged_files}, out_file, indent=4, ensure_ascii=False)