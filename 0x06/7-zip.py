#!/usr/bin/python
"""A module that handles multiple exceptions"""

try:
    result = []
    list1 = [10, 20, 30, 40]
    list2 = [2, 0, 5]

    for a, b in zip(list1, list2):
        if b == 0: 
            result.append("Division by zero error")
        else:
            result.append(a / b)
except ZeroDivisionError:
    print("Division by zero error")
except IndexError:
    print("list are not the same size")
else:
    print(result)
finally:
    print("Final execution")
