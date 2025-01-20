import os

def count_words_in_txt_files():
    # Get a list of all files in the current directory
    files_in_directory = os.listdir('.')
    
    # Filter for .txt files
    txt_files = [file for file in files_in_directory if file.endswith('.txt')]
    
    # Initialize a dictionary to store file names and their word counts
    word_counts = {}
    
    # Count words in each .txt file
    for txt_file in txt_files:
        try:
            with open(txt_file, 'r', encoding='utf-8') as file:
                content = file.read()
                word_count = len(content.split())
                word_counts[txt_file] = word_count
        except Exception as e:
            print(f"Error reading {txt_file}: {e}")
    
    # Display results
    if word_counts:
        print("Word counts in .txt files:")
        for file, count in word_counts.items():
            print(f"{file}: {count} words")
    else:
        print("No .txt files found in the current directory.")

if __name__ == "__main__":
    count_words_in_txt_files()
