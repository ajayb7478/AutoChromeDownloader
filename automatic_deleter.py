import os
import shutil

def delete_and_execute():
    try:
        # Specify the folder path (current directory in this case)
        folder_path = "Downloads"

        # Check if the folder exists
        if os.path.exists(folder_path):
            # Use shutil.rmtree to delete the entire folder and its contents
            shutil.rmtree(folder_path)
            #print(f" Folder {downloads_folder_path} and its contents deleted successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Call the function
