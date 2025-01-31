import json
import os

# Load the input JSON file
with open("input.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Transform the "findings" dictionary to strip the file paths
new_findings = {os.path.basename(file_path): findings for file_path, findings in data["findings"].items()}

# Update the JSON structure
data["findings"] = new_findings

# Save the output JSON file
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Transformed JSON file has been created: output.json")
