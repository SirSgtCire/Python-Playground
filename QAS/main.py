# Main file for running test strategies
import csv
import os
import sys
import pytest
import urllib3
import appconf
import argparse
import test_selenium


def __main__():
    print("Welcome to Quality Assurance Strategies")
    # Initialize project
    config = get_cmd_line_args()
    appconf.load(config)
    # Run Selenium Tests
    run_selenium_tests()
    # TODO: Run Other Tests


def get_cmd_line_args():
    parser = argparse.ArgumentParser(description='Parser for loading in command line parameters')
    parser.add_argument('--cfgfile', action="store", dest="cfgfile", default="QAS/default.json",
                        help="Give the name of a valid config.json file you wish to load into the program.")
    result = parser.parse_args()
    return result.cfgfile


def run_selenium_tests():
    print("Running dedicated suite of tests for Selenium UI")
    test_selenium.test_browser_check()


def find_file(filename, search_path):
    print(f"Finding {filename} somewhere within {search_path}")
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    return None


if __name__ == "__main__":
    __main__()
