#!/usr/bin/python
"""A module that handles python string formatting"""
name = "john"
age = 30
price = 49.99
formatedprice = "the prize is {} dollars ".format(price)
formatedstring = "my name is {} and i am {} years old".format(name,age)
print(formatedstring)
print(formatedprice)
