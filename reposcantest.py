import os
import csv
import json
from bs4 import BeautifulSoup
from datetime import datetime

def load_forbidden_terms(csv_path):
    """Load forbidden terms from CSV file."""
    forbidden_terms = []
    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            forbidden_terms.extend(row)
    return forbidden_terms

def scan_html_file(file_path, forbidden_terms):
    """Scan a single HTML file for forbidden terms."""
    findings = []
    
    with open(file_path, 'r', encoding='utf-8') as file:
        # Read file lines for line number tracking
        lines = file.readlines()
        
        # Join lines for BeautifulSoup parsing
        html_content = ''.join(lines)
        
        # Parse HTML and get text content
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Check each line for forbidden terms
        for line_num, line in enumerate(lines, 1):
            for term in forbidden_terms:
                if term.lower() in line.lower():
                    findings.append({
                        'term': term,
                        'line_number': line_num,
                        'line_content': line.strip()
                    })
    
    return findings

def scan_directory(directory_path, csv_path):
    """Recursively scan directory for HTML files and check for forbidden terms."""
    forbidden_terms = load_forbidden_terms(csv_path)
    results = {
        'scan_date': datetime.now().isoformat(),
        'total_files_scanned': 0,
        'files_with_findings': 0,
        'findings': {}
    }
    
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, directory_path)
                
                findings = scan_html_file(file_path, forbidden_terms)
                results['total_files_scanned'] += 1
                
                if findings:
                    results['files_with_findings'] += 1
                    results['findings'][relative_path] = findings
    
    return results

def save_results(results, output_path):
    """Save scan results to JSON file."""
    with open(output_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(results, jsonfile, indent=2)

def main():
    # Configure these paths as needed
    directory_to_scan = './html_files'
    forbidden_terms_csv = 'forbiddenphrases.csv'
    output_json = f'scan_results_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
    
    try:
        results = scan_directory(directory_to_scan, forbidden_terms_csv)
        save_results(results, output_json)
        
        print(f"Scan completed:")
        print(f"Total files scanned: {results['total_files_scanned']}")
        print(f"Files with findings: {results['files_with_findings']}")
        print(f"Results saved to: {output_json}")
        
    except Exception as e:
        print(f"Error during scan: {str(e)}")

if __name__ == "__main__":
    main()