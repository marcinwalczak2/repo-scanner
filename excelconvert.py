import json
import pandas as pd
from pathlib import Path

def convert_json_to_excel(json_data, output_file='findings_report.xlsx'):
    """
    Convert JSON findings data to Excel format.
    
    Args:
        json_data (dict): The JSON data containing the findings
        output_file (str): Name of the output Excel file
    """
    # Create a list to store all records
    records = []
    
    # Extract findings from the JSON data
    findings = json_data.get('findings', {})
    
    # Iterate through each file and its findings
    for filename, file_findings in findings.items():
        for finding in file_findings:
            record = {
                'Filename': filename,
                'Term': finding['term'],
                'Line Number': finding['line_number'],
                'Line Content': finding['line_content']
            }
            records.append(record)
    
    # Convert to DataFrame
    df = pd.DataFrame(records)
    
    # Sort by filename and line number
    df = df.sort_values(['Filename', 'Line Number'])
    
    # Write to Excel
    df.to_excel(output_file, index=False)
    print(f"Excel file created successfully: {output_file}")
    
    # Print summary statistics
    print("\nSummary:")
    print(f"Total findings: {len(df)}")
    print("\nFindings per file:")
    print(df['Filename'].value_counts())
    print("\nMost common terms:")
    print(df['Term'].value_counts().head())

# Example usage
if __name__ == "__main__":
    # Read the JSON file
    input_file = "paste.txt"  # Change this to your input file name
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Convert to Excel
        convert_json_to_excel(data)
        
    except FileNotFoundError:
        print(f"Error: Could not find input file '{input_file}'")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in input file")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {str(e)}")