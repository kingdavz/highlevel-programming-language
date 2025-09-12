#!/usr/bin/python
"""A module that implements continue statement"""

for i in range(1, 11):
    if i == 5 or i == 6:
        continue
    print(i, end=" ")
