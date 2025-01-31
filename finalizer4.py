import json
import os

def merge_json_files(json1_path, json2_path, output_path):
    # Load JSON1 (scan results)
    with open(json1_path, "r", encoding="utf-8") as file1:
        json1 = json.load(file1)

    # Load JSON2 (file metadata)
    with open(json2_path, "r", encoding="utf-8") as file2:
        json2 = json.load(file2)

    # Extract findings
    findings = json1.get("findings", {})

    # Create a lookup dictionary from json2 (title & name metadata)
    metadata_lookup = {}
    for entry in json2:
        filename = entry["filename"]
        base_filename = os.path.splitext(filename)[0]  # Remove .htm/.html extension
        metadata_lookup[base_filename] = {"title": entry["title"], "name": entry["name"]}

    merged_data = []

    for html_file, terms in findings.items():
        base_html_file = os.path.splitext(html_file)[0]  # Remove .html to match JSON2
        metadata = metadata_lookup.get(base_html_file, {"title": "Unknown Title", "name": "Unknown Name"})
        
        merged_data.append({
            "html_file": html_file,
            "title": metadata["title"],
            "name": metadata["name"],
            "findings": sorted(terms, key=lambda x: (x["term"], x["line_number"]))
        })

    # Sort merged data by html_file name
    merged_data.sort(key=lambda x: x["html_file"])

    # Save final output
    with open(output_path, "w", encoding="utf-8") as outfile:
        json.dump({"files": merged_data}, outfile, indent=4)

# Example usage
merge_json_files("C:\\Code\\Repo Scan Test\\scan_results_20250131_012857.json", "C:\\Code\\Repo Scan Test\\NameList\\NameJson\\combined_toc_entries.json", "C:\\Code\\Repo Scan Test\\LIST3.json")