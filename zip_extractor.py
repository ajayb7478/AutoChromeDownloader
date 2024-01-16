import os
import zipfile
def unzipper():
    # Set the path to the downloads folder
    downloads_folder = "Downloads"
    # Set the name of the zip file
    zip_file_name = "Rocket Flyer.zip"
    # Construct the full path to the zip file
    zip_file_path = os.path.join(downloads_folder, zip_file_name)

    # Check if the zip file exists
    if os.path.exists(zip_file_path):
        # Create a ZipFile object
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            # Extract all contents to the root folder
            zip_ref.extractall()

        print(f"{zip_file_name} has been successfully extracted.")
    else:
        print(f"{zip_file_name} not found in the {downloads_folder} folder.")
