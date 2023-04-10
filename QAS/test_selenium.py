import appconf

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
import json
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def find_file(filename):
    for root, dirs, files in os.walk(os.getcwd()):
        if filename in files:
            return os.path.join(root, filename)
    raise ValueError(f"{filename} not found in directory tree")


@pytest.fixture(scope="session")
def chrome_driver():
    # Use Chrome driver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.binary_location = find_file("chromedriver")
    driver_path = ChromeDriverManager().install()
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(options=options, service=service)

    yield driver

    driver.quit()


def test_config():
    # Open the configuration file and verify each necessary parameter for the tests in this file is present.
    config_file = "default.json"
    appconf.load(config_file)
    with open(config_file, "r") as f:
        config_blob = json.load(f)
        for key, value in config_blob.items():
            logger.debug("Do we make it here, and what do we get? %s, %s...", key, value)
        assert config_blob["google_home"] == appconf.google_home
        assert config_blob["driver_location"] == appconf.driver_location
        assert config_blob["report_location"] == appconf.report_location


def test_create_folders():
    # Ensure all subdirectories needed for this file are created.
    # Check if directory already exists
    if not os.path.exists(appconf.driver_location):
        # Create directory and log creation time
        os.makedirs(appconf.driver_location)
        logger.debug("Directory created successfully!")
    else:
        logger.debug("Directory already exists!")

    # Check if directory already exists
    if not os.path.exists(appconf.report_location):
        # Create directory and log creation time
        os.makedirs(appconf.report_location)
        logger.debug("Directory created successfully!")
    else:
        logger.debug("Directory already exists!")

    # Verify folder creation separately from actual creation
    assert os.path.exists(appconf.driver_location)
    assert os.path.exists(appconf.report_location)


def test_browser(chrome_driver):
    # Navigate to Google
    chrome_driver.get(appconf.google_home)

    # Check that the page title is "Google"
    assert chrome_driver.title == 'Google'
