import selenium_auto_downloader
import automatic_deleter
import version_checker
import zip_extractor
import exe_launcher

# Define the number of iterations

automatic_deleter.delete_and_execute()

if version_checker.check_version():
    print("New Build Available.")    
    print("Attempting to download the New Build using Browser")   
    selenium_auto_downloader.BrowserDownloader()     
    zip_extractor.unzipper()  
    automatic_deleter.delete_and_execute()
    input("Press Enter to Launch the game")
    exe_launcher.game_launcher_script()  
else:    
    print("Build is already on the latest version")
    input("Press Enter to Launch the game")
    exe_launcher.game_launcher_script()