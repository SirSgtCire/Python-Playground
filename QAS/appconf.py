from collections import OrderedDict
import json
import sys


def load(cfg_file):
    """Load configuration values from a JSON file."""
    config_data = json.load(open(cfg_file), object_pairs_hook=OrderedDict)
    # Begin process of loading our json variables into our appconf module.
    thismodule = sys.modules[__name__]
    for key in config_data.keys():
        value = config_data[key]
        # Explicitly check to see if the key in the json file exists within the appconf module.
        if hasattr(thismodule, key):
            setattr(thismodule, key, value)
        # If it isn't, we don't set it to anything and instead throw a ValueError.
        else:
            raise ValueError("The key \"{}\" provided in your json file was not found in appconf.py".format(key))
    # Explicitly check to see if all the variables in appconf.py have a value other than None.
    for item in dir(thismodule):
        if not item.startswith("__") and getattr(thismodule, item) is None:
            raise ValueError("The variable \"{}\" provided in appconf.py was not given any value".format(item))


# List of variable names found in default.json, to complete variable mapping within the application
google_home = None
driver_location = None
supported_browsers = None
