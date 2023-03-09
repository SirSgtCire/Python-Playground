from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.safaridriver import SafariDriverManager
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.microsoft import EdgeDriverManager
from webdriver_manager.iedriver import IEDriverManager
import os
import time

# create directory if it doesn't exist
driver_dir = os.path.join(os.getcwd(), 'drivers')
if not os.path.exists(driver_dir):
    os.makedirs(driver_dir)

# download and install the latest version of ChromeDriver to the directory
chrome_driver_path = ChromeDriverManager(path=driver_dir).install()

# download and install the latest version of GeckoDriver (Firefox) to the directory
firefox_driver_path = GeckoDriverManager(path=driver_dir).install()

# use the Chrome driver to open a website
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('https://www.google.com')
# wait for the browser to close
while len(driver.window_handles) > 0:
    time.sleep(1)

# use the Firefox driver to open a website
driver = webdriver.Firefox(executable_path=firefox_driver_path)
driver.get('https://www.google.com')
# wait for the browser to close
while len(driver.window_handles) > 0:
    time.sleep(1)

# close the driver when done
driver.quit()