import os
import streamlit as st
from PIL import Image
from pillow_heif import register_heif_opener

# Register the HEIF opener
register_heif_opener()

def batch_convert_heic_to_jpg(directory, max_width=800, max_height=600, optimize=False):
    """
    Converts all HEIC images in a given directory to JPG.

    Args:
        directory (str): Path to the directory containing HEIC files.
        max_width (int): Maximum width of the output image. Defaults to 800.
        max_height (int): Maximum height of the output image. Defaults to 600.
        optimize (bool): Whether to optimize the output JPG files for smaller size. Defaults to False.
    
    Raises:
        FileNotFoundError: If the specified directory does not exist.
        NotADirectoryError: If the specified path is not a directory.
    """

    # Check if the provided directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The specified directory '{directory}' does not exist.")
    
    # Check if the provided path is indeed a directory
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"'{directory}' is not a valid directory.")

    success_count = 0
    failure_count = 0

    for filename in os.listdir(directory):
        if filename.lower().endswith(".heic"):  # Case-insensitive check
            input_file_path = os.path.join(directory, filename)
            output_file_path = os.path.splitext(input_file_path)[0] + ".jpg"
            
            try:
                with Image.open(input_file_path) as img:
                    width, height = img.size
                    
                    # Calculate the scaling factor based on the maximum dimensions
                    scale_factor = min(max_width / width, max_height / height)
                    
                    # Resize the image while maintaining its aspect ratio
                    new_size = (int(width * scale_factor), int(height * scale_factor))
                    img_small = img.resize(new_size)
                    
                    if optimize:
                        img_small.convert('RGB').save(output_file_path, "JPEG", quality=90)
                    else:
                        img_small.convert('RGB').save(output_file_path, "JPEG")
                st.write(f"{filename} converted successfully!")
                success_count += 1
            except Exception as e:
                st.error(f"Failed to convert {filename}: {e}")
                failure_count += 1
                
    st.write("\nConversion Summary:")
    st.write(f"Successful conversions: {success_count}")
    st.write(f"Failed conversions: {failure_count}")

def main():
    st.title("HEIC to JPG Converter")

    # Get the directory path from the user
    directory = st.text_input("Enter the path to the folder containing HEIC files:")

    # Ask if they want to optimize the output JPG files
    optimize = st.checkbox("Optimize the output JPG files for smaller size")

    # Get the maximum width and height from the user
    col1, col2 = st.columns(2)
    max_width = col1.number_input("Maximum Width:", value=800)
    max_height = col2.number_input("Maximum Height:", value=600)

    # Create a button to start the conversion process
    if st.button("Start Conversion"):
        try:
            batch_convert_heic_to_jpg(directory, max_width=max_width, max_height=max_height, optimize=optimize)
        except (FileNotFoundError, NotADirectoryError) as e:
            st.error(e)

if __name__ == "__main__":
    main()