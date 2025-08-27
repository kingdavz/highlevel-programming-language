#!/usr/bin/python
"""A module that handles assignment operations"""
num = int(input("enter any number of your choice: "))

num += 2 # short hand
#num = num + 2 # opposite
print("Addition assignment {}".format(num))

num *= 2
print("Multiplication assignment {}".format(num))

num -= 2
print("Subtraction assignment {}".format(num))

num /= 2
print("Division assignment {}".format(num))

num %= 2
print("Modulus assignment {}".format(num))

num **= 2
print("Exponential assignment {}".format(num))