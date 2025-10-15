#!/usr/bin/python
"""A module that handles errors and exceptions"""

try:
    num = int(input("Enter a number: "))
    if not isinstance(num, int):
        raise ValueError("invalid data type")
except Exception as e:
    print(e)
