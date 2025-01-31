import json

def merge_json_files(json1_data, json2_data):
    # Create a lookup dictionary from json2 data
    filename_lookup = {
        item['filename']: {
            'title': item['title'],
            'name': item['name']
        } for item in json2_data
    }
    
    # Create new merged data structure
    merged_data = {
        "files": []
    }
    
    # Iterate through json1 files
    for file_entry in json1_data['files']:
        # Get the HTML filename
        html_file = file_entry['html_file']
        
        # Look for corresponding entry in json2
        if html_file in filename_lookup:
            # Create new entry with merged data
            new_entry = {
                'html_file': html_file,
                'title': filename_lookup[html_file]['title'],
                'name': filename_lookup[html_file]['name'],
                'findings': file_entry['findings']
            }
            merged_data['files'].append(new_entry)
    
    return merged_data

# Example usage:
def main():
    # Read the first JSON file with UTF-8 encoding
    with open('json1.json', 'r', encoding='utf-8') as f:
        json1_data = json.load(f)
    
    # Read the second JSON file with UTF-8 encoding
    with open('json2.json', 'r', encoding='utf-8') as f:
        json2_data = json.load(f)
    
    # Merge the data
    merged_data = merge_json_files(json1_data, json2_data)
    
    # Write the merged data to a new JSON file with UTF-8 encoding
    with open('merged_output.json', 'w', encoding='utf-8') as f:
        json.dump(merged_data, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()