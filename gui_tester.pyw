import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
import threading
import atexit
import selenium_auto_downloader
import automatic_deleter
import version_checker
import zip_extractor
import exe_launcher
import sys
import time

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Stellar Ascend")
        self.root.geometry("550x500")  # Increased width to accommodate the image and the text widget
        
         # Set the icon for the main window
        self.root.iconbitmap(default=sys._MEIPASS + "/icon.ico")  # Replace with the actual path to your icon file

        # Create GUI components
        self.label = tk.Label(root, text="Stellar Ascend", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.version_container = tk.Frame(root)
        self.version_container.pack(pady=10, anchor="w")

        
        
        self.status_label = tk.Label(root, text="Checking for updates...", font=("Helvetica", 12), wraplength=250)
        self.status_label.pack(pady=10, padx=10, anchor="w")

        # Load and display an image in a separate container
        self.image_container = tk.Frame(root)
        self.image_container.pack(pady=10)
        self.load_image("rbbx.png")  # Replace with the actual path to your image

        self.version_label = tk.Label(self.version_container, text="", font=("Helvetica", 12))
        self.version_label.pack(side=tk.LEFT, padx=10)

        self.update_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
        self.update_text.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.launch_button = tk.Button(root, text="Launch Game", command=self.launch_game, state=tk.DISABLED)
        self.launch_button.pack(pady=50, padx=50, side=tk.BOTTOM)

        # Start the update process automatically when the app opens
        self.root.after(100, self.check_updates)  # Delay the update check by 100 milliseconds

        # Bind the event handler for window close
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        # Register function to be called at exit
        atexit.register(self.cleanup)

    def check_updates(self):
        automatic_deleter.delete_and_execute()

        if version_checker.check_version():
            self.update_status_label("New Build Available. Downloading...")
            threading.Thread(target=self.download_update).start()
        else:
            self.update_status_label("Build is already on the latest version")
            self.enable_launch_button()

        version_text, update_description = self.read_version_and_description()
        self.version_label["text"] = "Version: " + version_text
        self.update_text.insert(tk.END, update_description)

    def load_image(self, path):
        try:
            image_path = sys._MEIPASS + "/" + path
            image = Image.open(image_path)
            image = image.resize((200, 200), resample=Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            image_label = tk.Label(self.image_container, image=photo)
            image_label.image = photo  # To prevent the image from being garbage collected
            image_label.pack(side=tk.LEFT, padx=10)
        except Exception as e:
            print(f"Error loading image: {e}")


    def read_version_and_description(self):
        try:
            with open("Version/version.txt", "r") as file:
                lines = file.readlines()
                version_text = lines[0].strip()
                update_description = "\n".join(lines[1:])
                return version_text, update_description
        except FileNotFoundError:
            return "File not found", ""

    def download_update(self):
        selenium_auto_downloader.BrowserDownloader()
        self.update_status_label("Installing the game.....")
        time.sleep(2)
        zip_extractor.unzipper()
        automatic_deleter.delete_and_execute()
        self.root.after(0, self.update_status_label, "Update Complete. Ready to launch.")
        self.root.after(0, self.enable_launch_button)

    def enable_launch_button(self):
        self.launch_button["state"] = tk.NORMAL

    def launch_game(self):
        threading.Thread(target=self.launch_game_thread).start()

    def launch_game_thread(self):
        exe_launcher.game_launcher_script()
        sys.exit()

    def on_close(self):
        self.cleanup()
        sys.exit()

    def cleanup(self):
        if hasattr(self, 'root') and self.root is not None:
            self.root.destroy()

    def update_status_label(self, message):
        self.status_label["text"] = message

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
