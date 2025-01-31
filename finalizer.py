import json
from collections import defaultdict
from pathlib import Path

def combine_team_phrases(list1_path, combined_json_path, output_filename):
    try:
        # Load LIST1 (forbidden phrases scan results)
        with open(list1_path, 'r', encoding='utf-8') as f:
            phrase_data = json.load(f)
            
        # Load combined JSON (team assignments)
        with open(combined_json_path, 'r', encoding='utf-8') as f:
            team_data = json.load(f)
            
        # Create a lookup dictionary for team assignments
        # Key: filename, Value: (name, title) tuple
        team_lookup = {
            item['filename']: (item['name'], item['title']) 
            for item in team_data
        }
        
        # Create a defaultdict to organize data by team member
        team_phrases = defaultdict(lambda: defaultdict(list))
        
        # Process each HTML file from LIST1
        for html_file, phrases in phrase_data.items():
            # Check if this HTML file exists in team assignments
            if html_file in team_lookup:
                team_name, title = team_lookup[html_file]
                
                # Create phrase entries with all required information
                processed_phrases = []
                for phrase in phrases:
                    processed_phrase = {
                        'title': title,
                        'html_file': html_file,
                        'term': phrase['term'],
                        'line_number': phrase['line_number'],
                        'line_content': phrase['line_content']
                    }
                    team_phrases[team_name][html_file].append(processed_phrase)
        
        # Convert defaultdict to regular dict for JSON serialization
        output_data = {}
        for team_name, html_files in team_phrases.items():
            output_data[team_name] = dict(html_files)
        
        # Write the combined data to LIST3
        with open(output_filename, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2)
            
        print(f"\nSuccess! Combined data written to: {output_filename}")
        print(f"Total team members with assignments: {len(output_data)}")
        
        # Print summary of assignments
        for team_name, files in output_data.items():
            phrase_count = sum(len(phrases) for phrases in files.values())
            print(f"- {team_name}: {len(files)} files, {phrase_count} phrases")
            
        return output_filename
        
    except FileNotFoundError as e:
        print(f"Error: Could not find file - {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format - {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return None

# Example usage
if __name__ == "__main__":
    list1_path = "C:\\Code\\Repo Scan Test\\scan_results_20250131_012857.json"  # Replace with path to LIST1
    combined_json_path = "C:\\Code\\Repo Scan Test\\NameList\\NameJson\\combined_toc_entries.json"  # Replace with path to combined JSON
    output_filename = "LIST3.json"  # Output filename
    
    result = combine_team_phrases(list1_path, combined_json_path, output_filename)