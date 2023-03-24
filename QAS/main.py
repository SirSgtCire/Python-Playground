# Main file for running test strategies
# make sure to do imports here
import os
import sys
import pytest
import urllib3
import appconf
import argparse
import seleniumtest

def __main__():
	# Run all necessary functions here
	print("Welcome to Quality Assurance Strategies")
	# Run Selenium Tests

def get_cmd_line_args():
    parser = argparse.ArgumentParser(description='Parser for loading in command line parameters')
    parser.add_argument('--cfgfile', action="store", dest="cfgfile", default="default.json",
                        help="Give the name of a valid config.json file you wish to load into the program.")
    result = parser.parse_args()
    return result.cfgfile