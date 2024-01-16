import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def BrowserDownloader():
    # Get the current working directory
    current_directory = os.getcwd()
    # Define the relative path for the download folder
    download_folder = 'Downloads'
    # Combine the current directory and download folder to get the full path
    download_directory = os.path.join(current_directory, download_folder)
    # Make sure the download folder exists, create it if not
    if not os.path.exists(download_directory):
        os.makedirs(download_directory)
    # Configure Chrome options
    chrome_options = webdriver.ChromeOptions()
    prefs = {'download.default_directory': download_directory}
    chrome_options.add_experimental_option('prefs', prefs)
    chrome_options.add_argument("--start-maximized")
    # Create the Chrome WebDriver with options
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://drive.usercontent.google.com/download?id=10eHbV3t3lxGAQkpILwrMbAcwj7xMuL5A&export=download&authuser=0")       
    try:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#uc-download-link")))
    # Click the element once it's clickable
        element.click()        
    except Exception as e:
        print(f"Error: {e}")         
    driver.get("chrome://downloads/")     
    try:
        # Wait for the file to appear in the download directory
        WebDriverWait(driver, 300).until(lambda x: any(file.endswith('.crdownload') for file in os.listdir(download_directory))
        )
        # Wait for the file to be completely downloaded
        WebDriverWait(driver, 300).until(lambda x: not any(file.endswith('.crdownload') for file in os.listdir(download_directory))
        )
    finally:
        #This will close the browser window, even if an exception occurs
        driver.quit()