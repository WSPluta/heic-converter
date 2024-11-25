import os
from PIL import Image
from pillow_heif import register_heif_opener

# Register the HEIF opener
register_heif_opener()

def batch_convert_heic_to_png(directory):
    """
    Converts all HEIC images in a given directory to PNG.

    Args:
        directory (str): Path to the directory containing HEIC files.
    
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
            output_file_path = os.path.splitext(input_file_path)[0] + ".png"
            
            try:
                with Image.open(input_file_path) as img:
                    img.save(output_file_path, "PNG")
                print(f"{filename} converted successfully!")
                success_count += 1
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")
                failure_count += 1
                
    print(f"\nConversion Summary:")
    print(f"Successful conversions: {success_count}")
    print(f"Failed conversions: {failure_count}")

def main():
    # Ask for input folder path from the user
    while True:
        directory = input("Please enter the path to the folder containing HEIC files: ")
        
        try:
            batch_convert_heic_to_png(directory)
            break
        except (FileNotFoundError, NotADirectoryError) as e:
            print(e)
            response = input("Would you like to retry? (yes/no): ")
            if response.lower() != 'yes':
                break

if __name__ == "__main__":
    main()