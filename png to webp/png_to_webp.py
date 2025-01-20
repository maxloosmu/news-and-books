from PIL import Image

# File paths
input_file = "test.png"
output_file = "test.webp"

def convert_png_to_webp(input_path, output_path):
    try:
        # Open the input PNG image
        with Image.open(input_path) as img:
            # Convert and save as WebP
            img.save(output_path, format="WEBP", lossless=True)
        print(f"Conversion successful! Saved as {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Execute the conversion
convert_png_to_webp(input_file, output_file)
