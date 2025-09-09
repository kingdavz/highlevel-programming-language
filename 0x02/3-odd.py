#!/usr/bin/python
"""A module that implements odd number using for loop"""

for i in range(1, 11, 2):
    print(i)

for i in range(0, 11):
    if i & 1 == 1:
        print(i)
    else:
        continue