#!/usr/bin/python
"""A module that adds elements to a dictionary"""

vehicle = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(vehicle.get ("brand"))
print(vehicle.get("model"))
print(vehicle.get("year"))

# using index
print(vehicle["brand"])
print(vehicle["model"])
print(vehicle["year"])