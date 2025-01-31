import json

# Load JSON files
with open("json1.json", "r", encoding="utf-8") as f1:
    json1 = json.load(f1)

with open("json2.json", "r", encoding="utf-8") as f2:
    json2 = json.load(f2)

# Convert json2 into a dictionary for quick lookup
json2_dict = {entry["filename"]: {"title": entry["title"], "name": entry["name"]} for entry in json2}

# Create the merged JSON structure
merged_json = {"files": []}

for file_entry in json1["files"]:
    html_file = file_entry["html_file"]
    if html_file in json2_dict:
        # Merge data
        file_entry["title"] = json2_dict[html_file]["title"]
        file_entry["name"] = json2_dict[html_file]["name"]
        merged_json["files"].append(file_entry)

# Save the merged JSON
with open("merged.json", "w", encoding="utf-8") as f_out:
    json.dump(merged_json, f_out, indent=4, ensure_ascii=False)

print("Merged JSON saved as merged.json")
