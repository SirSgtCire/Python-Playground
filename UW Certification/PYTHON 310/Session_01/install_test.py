#!/usr/bin/env python3

import sys
print("This is my first python program")

version = sys.version_info

if version.major == 3:
    if version.minor < 9:
        print("You should be running version 3.9 or higher")
    else:
        print("I am running python {}.{} -- all good!".format(
               version.major, version.minor))

else:
    print("You need to run Python 3!")
    print("This is version: {}.{}".format(version.major, version.minor))