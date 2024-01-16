import os
import requests

def check_version():
    # URL of the raw GitHub file
    print("Checking for new Build.......")
    github_url = "https://raw.githubusercontent.com/ajayb7478/ajayb7478.github.io/main/Version.txt"

    # Local path to save the downloaded file
    local_folder = "Version"
    local_path = os.path.join(local_folder, "Version.txt")

    # Create the "Version" folder if it doesn't exist
    if not os.path.exists(local_folder):
        os.makedirs(local_folder)
        
    # Read existing content from the local file (if it exists)
    try:
        with open(local_path, "r") as file:
            existing_content = file.read()
    except FileNotFoundError:
        existing_content = ""

    # Download the content from the GitHub link
    response = requests.get(github_url)
    github_version = response.content.decode("utf-8")

    # Compare the contents and return True if there's a change
    if github_version != existing_content:
        # Update the local file with the new content
        with open(local_path, "w") as file:
            file.write(github_version)
        return True
    else:
        return False
