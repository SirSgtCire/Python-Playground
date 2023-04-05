import os
import main
import appconf
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.chrome.service import Service as BraveService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

approved_browsers_list = []


def test_browser_check():
    # Initialize project
    config = main.get_cmd_line_args()
    appconf.load(config)

    # Create local test variables
    test_url = appconf.google_home
    custom_path = appconf.driver_location
    if not os.path.exists(custom_path):
        os.makedirs(custom_path)

    driver_path = appconf.driver_location  # Set the path to the directory where you want to install the driver binaries

    # Install the Chrome driver binary to the specified path
    chrome_driver_path = os.path.abspath(ChromeDriverManager(path=driver_path).install())
    print(f"Chrome driver path: '{chrome_driver_path}")

    # Create a Chrome webdriver instance using the installed driver binary
    chrome_options = ChromeOptions()
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

    # Open the driver
    driver.get(test_url)
    driver.maximize_window()
    print(driver.title)


def launch_driver(input_driver, input_url, input_browser):
    # Launch given driver
    input_driver.get(input_url)
    print(f'{input_browser} browser loaded successfully.')

    # Wait for the window to close
    wait = WebDriverWait(input_driver, 10)
    wait.until(EC.invisibility_of_element_located((By.TAG_NAME, 'body')))
    approved_browsers_list.append(input_browser)

    # Add browser to approved_browsers_list after closing the driver
    input_driver.quit()
    print(f'{input_browser} browser closed successfully.')
