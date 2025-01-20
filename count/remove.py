import os

def remove_lines_from_txt_files():
    # Get a list of all files in the current directory
    files_in_directory = os.listdir('.')
    
    # Filter for .txt files
    txt_files = [file for file in files_in_directory if file.endswith('.txt')]
    
    # Process each .txt file
    for txt_file in txt_files:
        try:
            # Read the file content
            with open(txt_file, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            
            # Remove lines that start with "See also: " or contain ", click here for Latest Section"
            modified_lines = [
                line for line in lines 
                if not line.startswith("See also: ") and ", click here for " not in line
            ]
            
            # Check if the file content has changed
            if lines != modified_lines:
                # Overwrite the file with the modified content
                with open(txt_file, 'w', encoding='utf-8') as file:
                    file.writelines(modified_lines)
                print(f"Updated file: {txt_file}")
            else:
                print(f"No changes made to file: {txt_file}")
        except Exception as e:
            print(f"Error processing {txt_file}: {e}")

if __name__ == "__main__":
    remove_lines_from_txt_files()
