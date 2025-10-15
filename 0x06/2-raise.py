#!/usr/bin/python
"""A module that divides two numbers"""

def div(a,b):
    """A module that divides two numbers"""
    return a/b

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise ValueError("invalid data type")
    if num2 == 0:
        raise ZeroDivisionError("division by zero is not allowed")
    else:
        eq = div(num1, num2)
        print(f"{num1} / {num2} = {eq}")
finally:
    print("End of program")