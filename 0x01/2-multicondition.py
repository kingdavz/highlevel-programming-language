#!/usr/bin/python
"""A module that handles conditional statements"""
age = int(input("enter your age:"))
if age >= 10 and age <= 17:
    print("you are a teenager:")
elif age >=18 and age <= 40:
    print("you are an adult:")
else:
    print("you are old")