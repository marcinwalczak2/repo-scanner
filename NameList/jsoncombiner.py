import json
import os
from pathlib import Path

def combine_json_files(input_folder, output_filename):
    # Initialize an empty list to store all entries
    combined_data = []
    
    try:
        # Get all JSON files from the input folder
        json_files = list(Path(input_folder).glob('*.json'))
        
        if not json_files:
            raise ValueError(f"No JSON files found in {input_folder}")
            
        print(f"Found {len(json_files)} JSON files to process...")
        
        # Process each JSON file
        for json_path in json_files:
            try:
                with open(json_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    
                    # Handle both single objects and lists of objects
                    if isinstance(data, list):
                        combined_data.extend(data)
                    else:
                        combined_data.append(data)
                        
                print(f"Processed: {json_path.name}")
                    
            except json.JSONDecodeError:
                print(f"Error: {json_path.name} is not a valid JSON file. Skipping...")
            except Exception as e:
                print(f"Error processing {json_path.name}: {str(e)}")
        
        # Write the combined data to a new JSON file
        output_path = Path(input_folder) / output_filename
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(combined_data, f, indent=4)
            
        print(f"\nSuccess! Combined JSON file created at: {output_path}")
        print(f"Total entries combined: {len(combined_data)}")
        
        return str(output_path)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

# Example usage
if __name__ == "__main__":
    # Specify the folder containing your JSON files
    input_folder = "C:\\Code\\Repo Scan Test\\NameList\\NameJson"  # Replace with your folder path
    
    # Specify the name for the combined output file
    output_filename = "combined_toc_entries.json"
    
    combined_file = combine_json_files(input_folder, output_filename)
    
    if combined_file:
        print(f"\nYou can find your combined file at: {combined_file}")