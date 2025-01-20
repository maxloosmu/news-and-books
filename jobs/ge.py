from collections import defaultdict

# File paths
input_file = "dump.txt"
output_file = "undump_output.txt"

def process_dump(input_path, output_path):
    with open(input_path, "r") as file:
        lines = file.readlines()

    category_map = defaultdict(list)
    current_category = None
    job_title = None

    for line in lines:
        line = line.strip()
        # Ignore unwanted lines
        if line.startswith(("undefined :", "Posted Date :", "Job ID :", "Job Description Summary.", "Location :")):
            continue

        if line.startswith("Category :"):
            # When a category is found, assign it
            current_category = line.split(":")[1].strip().upper()
            if job_title and current_category:
                # Pair the previous job title with the current category
                category_map[current_category].append(job_title)
                job_title = None  # Reset job title for the next one
        elif not current_category:
            # Treat the first line as the first job title
            job_title = line
        else:
            # Subsequent lines that are not categories are treated as job titles
            job_title = line

    # Write to output file
    with open(output_path, "w") as file:
        for category, titles in category_map.items():
            file.write(f"{category}\n")
            for title in titles:
                file.write(f"{title}\n")
            file.write("\n")

# Execute the processing
process_dump(input_file, output_file)
print(f"Processed data saved to {output_file}")
