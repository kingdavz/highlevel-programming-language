#!/usr/bin/python
"""A module that handles missin files"""
try:
    with open("example.txt", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError as e:
    print(e)