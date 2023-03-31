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

    driver_folder = os.path.join(os.getcwd(), custom_path)
    print(f"Driver folder: '{driver_folder}'")

    # Create each available browser driver available in Selenium 4
    chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(path=driver_folder).install()))

    chromium_driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(executable_path=driver_folder, chrome_type=ChromeType.CHROMIUM).install()))

    brave_driver = webdriver.Chrome(service=BraveService(ChromeDriverManager(executable_path=driver_folder, chrome_type=ChromeType.BRAVE).install()))

    gecko_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager(executable_path=driver_folder).install()))

    ie_driver = webdriver.Ie(service=IEService(IEDriverManager(executable_path=driver_folder).install()))

    edge_driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager(executable_path=driver_folder).install()))

    opera_options = webdriver.ChromeOptions()
    opera_options.add_argument('allow-elevated-browser')
    opera_options.binary_location = driver_folder
    opera_driver = webdriver.Opera(executable_path=OperaDriverManager().install(), options=opera_options)

    # Launch each driver loads successfully
    launch_driver(chrome_driver, test_url, "chrome")
    launch_driver(chromium_driver, test_url, "chromium")
    launch_driver(brave_driver, test_url, "brave")
    launch_driver(gecko_driver, test_url, "firefox")
    launch_driver(ie_driver, test_url, "ie")
    launch_driver(edge_driver, test_url, "edge")
    launch_driver(opera_driver, test_url, "opera")

    # Verify we made it through all of our browsers
    assert approved_browsers_list == 7, f"We did NOT make it through all of our browsers, here are the ones that passed: '{approved_browsers_list}'"


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
