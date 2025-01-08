import re
from collections import defaultdict

# Load and process the file
input_file = 'dump.txt'
output_file = 'undump_output.txt'

def process_file(input_file, output_file):
    # Step 1: Remove blank lines
    with open(input_file, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
    
    # Step 2: Capitalize unique headings from odd-numbered lines and pair with job titles
    grouped_data = defaultdict(list)
    for i in range(0, len(lines), 2):
        heading = lines[i].strip().upper()
        job_title = lines[i + 1].strip()
        grouped_data[heading].append(job_title)
    
    # Step 3: Write grouped data to output file
    with open(output_file, 'w') as file:
        for heading, titles in grouped_data.items():
            file.write(f"{heading}\n")
            for title in titles:
                file.write(f"{title}\n")
            file.write("\n")

# Run the processing
process_file(input_file, output_file)
