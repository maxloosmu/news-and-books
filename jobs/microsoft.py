# Script to convert dump.txt to undump.txt using line count

# Input and output file paths
input_file = 'dump.txt'
output_file = 'undump_output.txt'

def process_file(input_path):
    job_titles = []
    with open(input_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        # Process lines to extract job titles
        for i in range(len(lines)):
            line = lines[i].strip()
            # A job title is likely a single line with text, followed by metadata lines
            if line and i + 1 < len(lines) and lines[i + 1].strip() == '':  # Check the next line for job metadata
                job_titles.append(line)
    return job_titles

def save_to_file(output_path, job_titles):
    with open(output_path, 'w', encoding='utf-8') as file:
        for title in job_titles:
            file.write(title + '\n')

# Process the input file and save to output
job_titles = process_file(input_file)
save_to_file(output_file, job_titles)

print(f"Processed job titles saved to {output_file}.")
