#!/usr/bin/python
"""A module that displays both key and the value of a dictionary"""

person = {
    "name": "John Doe",
    "age": 50,
    "city": "new york",
    "friends": ["joy","abigail", "emmanuel"],
    "country": "united states"
}

for key, value in person.items():
    print(f"{key} -> {value}")