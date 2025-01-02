import csv
import requests
from bs4 import BeautifulSoup

# Define input and output file paths
input_file = 'url.csv'
output_file = 'url_updated.csv'

# Function to fetch the full title from a URL
def fetch_title(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an error for bad status codes
        soup = BeautifulSoup(response.text, 'html.parser')

        # Attempt to extract the full title from meta tags or other locations
        title_tag = soup.find('title')
        meta_title = soup.find('meta', attrs={'property': 'og:title'})

        if meta_title and 'content' in meta_title.attrs:
            title = meta_title['content'].strip()
        elif title_tag:
            title = title_tag.string.strip()
        else:
            title = 'No Title Found'

        return title
    except Exception as e:
        print(f"Error fetching title for URL {url}: {e}")
        return 'Error Fetching Title'

# Read the input CSV and process missing titles
try:
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames

        if 'URL' not in fieldnames or 'Title' not in fieldnames:
            raise ValueError("The CSV file must contain 'URL' and 'Title' headers.")

        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            if not row['Title'].strip():
                print(f"Fetching title for URL: {row['URL']}")
                row['Title'] = fetch_title(row['URL'].strip())
            writer.writerow(row)

    print(f"Updated CSV file saved as {output_file}.")

except FileNotFoundError:
    print(f"The file {input_file} does not exist.")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
