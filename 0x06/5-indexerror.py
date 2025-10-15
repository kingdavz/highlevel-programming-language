#!/usr/bin/python
"""A module that handles index error exception"""

try:
    fruits = ["apple", "banana", "orange"]
    print(fruits[2])
    print(fruits[3])
except IndexError:
    print("Index out of range")
finally:
    print("Execution complete")