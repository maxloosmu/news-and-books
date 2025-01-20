import os
from PIL import Image

def convert_all_png_to_webp():
    # Get the current directory
    current_dir = os.getcwd()

    # Iterate through all files in the directory
    for file_name in os.listdir(current_dir):
        # Check if the file is a PNG
        if file_name.lower().endswith('.png'):
            input_path = os.path.join(current_dir, file_name)
            output_path = os.path.splitext(input_path)[0] + '.webp'

            try:
                # Open the input PNG image
                with Image.open(input_path) as img:
                    # Convert and save as WebP
                    img.save(output_path, format="WEBP", lossless=True)
                print(f"Converted {file_name} to {output_path}")
            except Exception as e:
                print(f"An error occurred while converting {file_name}: {e}")

if __name__ == "__main__":
    convert_all_png_to_webp()
