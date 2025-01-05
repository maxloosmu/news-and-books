# Read the contents of LIST.txt
with open('JOBS.txt', 'r') as file:
    lines = file.readlines()

# Create an HTML ordered list
html_content = "<ol>\n"
for line in lines:
    html_content += f"    <li>{line.strip()}</li>\n"
html_content += "</ol>"

# Save the HTML content to HTML.txt
with open('htmlJOBS.txt', 'w') as file:
    file.write(html_content)

print("HTML content successfully written to HTML.txt.")
