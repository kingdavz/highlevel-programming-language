#!/usr/bin/usr
"""A module that validates the age"""

try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative")
except ValueError:
    print("Error: Age must be a number")
else:
    print(f"you are {age} years old.")
finally:
    print("execution complete")
