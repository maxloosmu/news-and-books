# Script to process URLs in new_urls.txt

# Read the file
file_path = 'new_urls.txt'

# Function to clean up the URL
def clean_url(url):
    # Remove the date-time part using the last "/"
    clean_url = url.rsplit('/', 1)[0]
    # Ensure the URL ends with a trailing slash
    if not clean_url.endswith('/'):
        clean_url += '/'
    return clean_url

# Process the file
with open(file_path, 'r') as file:
    urls = file.readlines()

# Clean each URL
cleaned_urls = [clean_url(url.strip()) for url in urls]

# Save the changes back to the same file
with open(file_path, 'w') as file:
    for url in cleaned_urls:
        file.write(url + '\n')
