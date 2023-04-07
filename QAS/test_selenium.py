import appconf
import tools

import os
import sys
import time
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeDriverService
from selenium.webdriver.edge.service import Service as EdgeDriverService
from selenium.webdriver.firefox.service import Service as GeckoDriverService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def test_browser():
    # Specify the path where you want to save the Chrome webdriver
    driver_path = tools.find_file("chromedriver", )

    # Download the Chrome webdriver to the specified path
    if not os.path.isfile(driver_path):
        print('Downloading Chrome webdriver...')
        driver_url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
        response = requests.get(driver_url)
        version_number = response.text.strip()
        if sys.platform.startswith('win'):
            driver_filename = 'chromedriver.exe'
        else:
            driver_filename = 'chromedriver'
        updated_driver_url = f'https://chromedriver.storage.googleapis.com/{version_number}/{driver_filename}'
        response = requests.get(updated_driver_url)
        with open(driver_path, 'wb') as f:
            f.write(response.content)

    # Set up the Chrome webdriver service
    service = Service(driver_path)
    service.start()

    # Open a new Chrome browser window
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(service=service, options=options)

    # Navigate to Google
    driver.get('https://www.google.com')

    # Wait for the page to load
    time.sleep(3)

    # Check that the page title is "Google"
    assert driver.title == 'Google'

    # Close the Chrome browser window
    driver.quit()
