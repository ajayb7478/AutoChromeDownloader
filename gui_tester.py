import tkinter as tk
import threading
import atexit
import selenium_auto_downloader
import automatic_deleter
import version_checker
import zip_extractor
import exe_launcher
import sys

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Updater")
        self.root.geometry("400x200")  # Set the initial size of the window

        # Create GUI components
        self.label = tk.Label(root, text="Automatic Updater", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.status_label = tk.Label(root, text="Checking for updates...", font=("Helvetica", 12))
        self.status_label.pack(pady=10)

        self.launch_button = tk.Button(root, text="Launch Game", command=self.launch_game, state=tk.DISABLED)
        self.launch_button.pack(pady=10)

        # Start the update process automatically when the app opens
        self.root.after(100, self.check_updates)  # Delay the update check by 100 milliseconds

        # Bind the event handler for window close
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        # Register function to be called at exit
        atexit.register(self.cleanup)

    def check_updates(self):
        # Function to check for updates
        automatic_deleter.delete_and_execute()

        if version_checker.check_version():
            self.update_status_label("New Build Available. Downloading...")
            # Perform download and update in a separate thread
            threading.Thread(target=self.download_update).start()
        else:
            self.update_status_label("Build is already on the latest version")
            self.enable_launch_button()

    def download_update(self):
        # Function to download and update
        selenium_auto_downloader.BrowserDownloader()
        zip_extractor.unzipper()
        automatic_deleter.delete_and_execute()

        # Update the status label and enable the launch button in the main thread
        self.root.after(0, self.update_status_label, "Update Complete. Ready to launch.")
        self.root.after(0, self.enable_launch_button)

    def enable_launch_button(self):
        # Function to enable the launch button
        self.launch_button["state"] = tk.NORMAL

    def launch_game(self):
        # Function to launch the game in a separate thread
        threading.Thread(target=self.launch_game_thread).start()

    def launch_game_thread(self):
        # Function to launch the game
        exe_launcher.game_launcher_script()

        # Close the app after launching the game
        sys.exit()

    def on_close(self):
        # Event handler for window close
        self.cleanup()
        sys.exit()

    def cleanup(self):
        # Function to destroy the Tkinter window
        self.root.destroy()

    def update_status_label(self, message):
        # Function to update the status label
        self.status_label["text"] = message

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
