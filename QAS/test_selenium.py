from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service as BraveService
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
import appconf
import os


def test_browser_check():
    # Define the custom path
    custom_path = appconf.driver_location
    if not os.path.exists(custom_path):
        os.makedirs(custom_path)

    # Define variable names
    test_url = appconf.google_home
    browser_list = appconf.supported_browsers

    # Install web browser drivers and launch each browser
    for browser in browser_list:
        if browser == "chrome":
            driver = webdriver.Chrome(executable_path=locate_file(custom_path, "chromedriver"))
        elif browser == "chromium":
            driver = webdriver.Chrome(executable_path=locate_file(custom_path, "chromiumdriver"))
        elif browser == "brave":
            driver = webdriver.Chrome(executable_path=locate_file(custom_path, "bravedriver"))
        elif browser == "firefox":
            driver = webdriver.Firefox(executable_path=locate_file(custom_path, "geckodriver"))
        elif browser == "ie":
            driver = webdriver.Ie(executable_path=locate_file(custom_path, "iedriver"))
        elif browser == "edge":
            driver = webdriver.Edge(executable_path=locate_file(custom_path, "edgedriver"))
        elif browser == "opera":
            driver = webdriver.Opera(executable_path=locate_file(custom_path, "operadriver"))
        else:
            print(f"{browser} is not a supported browser")
            continue

        # Launch browser and validate installation
        driver.get(test_url)
        print(driver.title)
        assert(driver.title is not None)
        driver.quit()


def locate_file(dir_path, file_name):
    # Walk through the directory and find the file
    for root, dirs, files in os.walk(dir_path):
        if file_name in files:
            # File found
            file_path = os.path.join(root, file_name)
            print(f"File found at: {file_path}")
            return file_path
    else:
        # File not found
        print(f"File '{file_name}' not found in directory '{dir_path}'")
    return "Error"
