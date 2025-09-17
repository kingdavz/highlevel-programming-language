#!/usr/bin/python
"""A module that shallow copies"""

fruits = ["Apple", "Conconut", "berry","Mango"]
copied_fruits = fruits

print(f"copied fruits {copied_fruits}")
fruits[1] = "banana"
print(f"copied list {copied_fruits}")
print(f"original list {fruits}")