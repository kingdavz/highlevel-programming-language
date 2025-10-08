#!/usr/bin/python
"""A module that can copy a file"""

import shutil

source = input("file to copy: ")
destination = input ("Where to copy it: ")

shutil.copyfile(source, destination)
print("file copied")