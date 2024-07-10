import os
import zipfile

# Define the directory containing the zip files
zip_directory = 'D:\serie\srt'

# Define the base directory where the files will be extracted
extract_base_directory = 'D:\serie\SCORPION (2014-2018) - Complete TV Series, Season 1,2,3,4 S01,S02,S03,S04 - 720p Web-DL x264'

# Ensure the base extraction directory exists
if not os.path.exists(extract_base_directory):
    os.makedirs(extract_base_directory)
    print(f'Created base extraction directory: {extract_base_directory}')

# Loop through the files in the zip directory
for filename in os.listdir(zip_directory):
    if filename.endswith('.zip'):
        # Construct full file path
        zip_path = os.path.join(zip_directory, filename)

        # Determine the target extraction directory from the zip file name
        extract_dir_name = os.path.splitext(filename)[0]  # Remove the .zip extension
        # Extract the season name (assuming 'season X' is at the beginning)
        season_name = extract_dir_name.split('(')[0].strip()

        # Construct the full extraction path
        extract_path = os.path.join(extract_base_directory, season_name)

        # Ensure the target directory exists
        if not os.path.exists(extract_path):
            os.makedirs(extract_path)
            print(f'Created extraction directory: {extract_path}')

        # Unzip the file to the target directory
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
            print(f'Extracted {filename} to {extract_path}')

print('Extraction completed.')
