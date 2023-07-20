from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import configparser
import os

# Function to transform user-inputted date
def transform_date(date_input):
    year, month, day = date_input.split('-')
    return month + day + year

def download_csv(date_input):
    # Load the credentials from the config.ini file
    config = configparser.ConfigParser()
    config.read('config.ini')
    username = config.get('credentials', 'username')
    password = config.get('credentials', 'password')
    downloads_folder = config.get('paths', 'downloads_folder')


    transformed_date = transform_date(date_input)

    # Set up the Selenium WebDriver (make sure you have installed the necessary browser driver)
    driver = webdriver.Chrome()  # Replace with the appropriate browser driver if using a different browser

    # Open the specific URL
    driver.get("https://trafinfo.com/sumner/viewlogs/login.php")

    # Find the login fields and enter the credentials
    username_field = driver.find_element(By.ID, "UC")
    password_field = driver.find_element(By.ID,"pass")

    username_field.send_keys(username)
    password_field.send_keys(password)

    # Submit the login form
    password_field.send_keys(Keys.RETURN)

    # Wait for the page to load after logging in
    time.sleep(1)

    # Find the input field and enter the transformed date
    date_field = driver.find_element(By.NAME, "date")
    date_field.clear()  # Clear the default value (today's date)
    date_field.send_keys(transformed_date)  # Input today's date in MMDDYYYY format
    date_field.send_keys(Keys.RETURN)

    # Wait for the download to complete (you may need to adjust the wait time based on the file size)
    time.sleep(2)

    # Close the browser
    driver.quit()

    file_path = os.path.join(downloads_folder, f"vms_log_{date_input}.txt")

    return file_path