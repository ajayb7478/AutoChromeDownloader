import os
import subprocess
def game_launcher_script():
    # Specify the folder and executable name
    folder_path = "Rocket Flyer"
    exe_name = "Rocket Flyer.exe"

    # Combine the folder and executable paths
    exe_path = os.path.join(folder_path, exe_name)

    # Check if the executable file exists
    if os.path.exists(exe_path):
        try:
            # Use subprocess to run the executable
            subprocess.run(exe_path)
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"Error: {exe_path} not found.")
