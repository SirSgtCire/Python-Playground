# File for commonly used definitions and functions
import os
import argparse


def get_cmd_line_args():
    parser = argparse.ArgumentParser(description='Parser for loading in command line parameters')
    parser.add_argument('--cfgfile', action="store", dest="cfgfile", default="default.json",
                        help="Give the name of a valid config.json file you wish to load into the program.")
    result = parser.parse_args()
    return result.cfgfile


def find_file(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
    return None
