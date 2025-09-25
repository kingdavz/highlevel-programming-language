#!/usr/bin/python
"""a module that performs set difference"""

num1 = set({1, 2, 3, 4})
num2 = {3, 4, 5, 6}

result = num1.difference(num2)

print(result)