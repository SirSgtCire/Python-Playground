from selenium import webdriver
from webdriver_manager.chrome.service import Service as ChromeService
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
import os
import time

test_url = "https://wwww.google.com"

# Install web browser drivers
chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
chromium_driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
brave_driver = webdriver.Chrome(service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))
firefox_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
ie_driver = webdriver.Ie(service=IEService(IEDriverManager().install()))
edge_driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
opera_driver = webdriver.Opera(executable_path=OperaDriverManager().install())

# Validate browser drivers installed successfully
chrome_driver.get(test_url)
print(chrome_driver.title)
chrome_driver.quit()

chromium_driver.get(test_url)
print(chromium_driver.title)
chromium_driver.quit()

brave_driver.get(test_url)
print(brave_driver.title)
brave_driver.quit()

firefox_driver.get(test_url)
print(firefox_driver.title)
firefox_driver.quit()

ie_driver.get(test_url)
print(ie_driver.title)
ie_driver.quit()

edge_driver.get(test_url)
print(edge_driver.title)
edge_driver.quit()

opera_driver.get(test_url)
print(opera_driver.title)
opera_driver.quit()
