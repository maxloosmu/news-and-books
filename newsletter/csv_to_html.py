import csv

# Define the input and output file paths
input_file = 'url_updated.csv'
output_file = 'html.txt'

# Initialize a list to store the HTML output
html_output = []

try:
    # Open the CSV file and read its contents
    with open(input_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        # Check if the required headers exist
        if 'URL' not in reader.fieldnames or 'Title' not in reader.fieldnames:
            raise ValueError("The CSV file must contain 'URL' and 'Title' headers.")

        # Process each row and format as HTML
        for row in reader:
            url = row['URL'].strip()
            title = row['Title'].strip()
            if url and title:  # Ensure both URL and Title are present
                html_output.append(f'<li>\n<a href="{url}">\n{title}\n</a>\n</li>')

    # Write the HTML output to a file
    with open(output_file, 'w', encoding='utf-8') as htmlfile:
        htmlfile.write('\n'.join(html_output))

    print(f"HTML content successfully saved to {output_file}.")

except FileNotFoundError:
    print(f"The file {input_file} does not exist.")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
