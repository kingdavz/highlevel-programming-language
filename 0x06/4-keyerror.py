#!/usr/bin/python
"""A module that handles key error exception"""

fruits = {"apple" : 2, "banana" : 3, "orange" : 0}

try:
    print(fruits.get("apple"))
    print(fruits["pawpaw"])
except KeyError:
    print("ket not found")
finally:
    print("Execution completed")