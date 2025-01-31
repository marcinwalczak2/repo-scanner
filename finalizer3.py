import json

# Load LIST1 (JSON output from the HTML scan)
with open('C:\\Code\\Repo Scan Test\\scan_results_20250131_012857.json', 'r') as file:
    list1 = json.load(file)

# Load LIST2 (JSON containing team member information)
with open('C:\\Code\\Repo Scan Test\\NameList\\NameJson\\combined_toc_entries.json', 'r') as file:
    list2 = json.load(file)

# Initialize LIST3
list3 = {}

# Iterate through LIST1
for html_file, phrases in list1.items():
    # Find the corresponding entry in LIST2
    for entry in list2:
        if entry['html_file_name'] == html_file:
            team_member = entry['team_member_name']
            title = entry['title']
            
            # If the team member is not already in LIST3, add them
            if team_member not in list3:
                list3[team_member] = []
            
            # Add the HTML file details to the team member's list
            for phrase in phrases:
                list3[team_member].append({
                    'html_file_name': html_file,
                    'title': title,
                    'term': phrase['term'],
                    'line_number': phrase['line_number'],
                    'line_content': phrase['line_content']
                })

# Save LIST3 as a JSON file
with open('LIST3.json', 'w') as file:
    json.dump(list3, file, indent=4)

print("LIST3 has been created and saved as LIST3.json")