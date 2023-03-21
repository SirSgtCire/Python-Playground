import datetime
import pytz
from collections import OrderedDict
import json
import sys
import ast


def format_file_name(date, node_type, subject_matter):
    return "{0.year}_{0.month}_{1}_{2}.csv".format(date, node_type, subject_matter)


def get_start_date():
    return get_date(start_date_values, start_time_values)


def get_end_date():
    return get_date(end_date_values, end_time_values)


def get_date(date_list, time_list):
    date_value = ast.literal_eval(date_list) + time_list
    return datetime.datetime(date_value[0], date_value[1], date_value[2], date_value[3],
                             date_value[4], date_value[5], date_value[6], pytz.UTC)


def load(cfg_file, start_date, end_date):
    """Load configuration values from a JSON file."""
    config_data = json.load(open(cfg_file), object_pairs_hook=OrderedDict)
    # Add start and end dates directly to the json object, to load into the appconf module later.
    config_data["start_date_values"] = start_date
    config_data["end_date_values"] = end_date
    thismodule = sys.modules[__name__]
    # Begin process of loading our json variables into our appconf module.
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


# Base API call to access all organizations on Rubicon Project Github.
api_call_base = None

# Alternative API call to use if given critical_repos_dictionary, which happens to be the core API call.
api_call_relevant = None

automated_users_list = None

irrelevant_files_list = None

start_date_values = None

end_date_values = None

start_time_values = None

end_time_values = None

critical_org_filenames = None

non_critical_org_filenames = None

org_field_names = None

critical_repo_filenames = None

non_critical_repo_filenames = None

repo_field_names = None

# Define specific dictionary for 'critical' repositories per organization (meaning production,
# front facing repositories) to use for further filtering at the repository level.
# All other organizations not defined in this dictionary will be ignored.
critical_repos_dictionary = None