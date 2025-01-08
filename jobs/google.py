# Script to process dump.txt and convert it to undump.txt format

# Input and output file paths
input_file = 'dump.txt'
output_file = 'undump_output.txt'

# List of keywords to remove lines containing only these words
keywords_to_remove = ["corporate_fare", "Google", "place", "Minimum qualifications", "Singapore", "Wing"]

def process_file(input_path):
    cleaned_lines = []
    with open(input_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Check if the line starts with spaces or tabs (without stripping)
            if line.startswith((' ', '\t')):
                continue
            # Remove lines containing only the specified keywords
            if line.strip() in keywords_to_remove:
                continue
            # Remove lines starting with "As an Alphabet company"
            if line.startswith("As an Alphabet company"):
                continue
            # Add to the result if it passes all checks
            cleaned_lines.append(line.rstrip())  # Remove trailing newlines only
    
    # Remove all blank lines from the final output
    cleaned_lines = [line for line in cleaned_lines if line.strip()]
    return cleaned_lines

def save_to_file(output_path, cleaned_lines):
    with open(output_path, 'w', encoding='utf-8') as file:
        for line in cleaned_lines:
            file.write(line + '\n')

# Process the input file and save to output
cleaned_lines = process_file(input_file)
save_to_file(output_file, cleaned_lines)

print(f"Processed content saved to {output_file}.")
