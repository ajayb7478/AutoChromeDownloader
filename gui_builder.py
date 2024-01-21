import os
import sys

# Get the path to the script's directory
script_dir = os.path.dirname(os.path.realpath(sys.argv[0]))

# Specify the paths to your image files
icon_path = os.path.join(script_dir, "icon.ico")
image_path = os.path.join(script_dir, "rbbx.png")

# Specify the --add-data option when running pyinstaller
pyinstaller_command = f"pyinstaller --onefile --add-data {icon_path};. --add-data {image_path};. gui_tester.py"

# Run the pyinstaller command
os.system(pyinstaller_command)
