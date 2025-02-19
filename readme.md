![Frontend](img/frontend.png)

# HEIC to JPG Converter
A simple Python script to convert HEIC images to JPG format.

## Requirements  

- Python 3.7+
- Pillow 9.2.0+
- pillow-heif 0.10.0+
- Streamlit 1.41.1

## Usage  

- Clone the repository: `git clone https://github.com/WSPluta/heic-converter.git`
- Navigate to the project directory: `cd heic-converter`
- Install the required libraries: `pip install -r requirements.txt`
- Run the script: `streamlit run main.py`
- Follow the prompts to select the input directory containing HEIC files.

## Features  

Converts all HEIC images in a given directory to PNG format
Preserves the original file names
Provides a summary of successful and failed conversions  

## Notes
This script uses the pillow-heif library to handle HEIC files. If you encounter any issues, please ensure you have the latest version installed.
This script is intended for personal use only. For commercial use, please consult the licenses of the used libraries.