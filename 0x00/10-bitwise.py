#!/usr/bin/python
"""A module that handles bitwise operations"""
num = int(input("Enter any number of your choice: "))

# left shift
print("left shift: {}".format(num << 1))

# right shift
print("right shift: {}".format(num >> 1))

# bitwise and
print("Bitwise and: {}".format(num & 1))

# bitwise or
print("Bitwise or: {}".format(num | 1))

# bitwise not
print("bitwise not: {}".format(~num))
