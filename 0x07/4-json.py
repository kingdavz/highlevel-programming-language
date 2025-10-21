#!/usr/bin/python 
"""A module that shows elements in a json file"""
import json

import json


countries = {
    "Nigeria": {"capital": "Abuja", "population": 200000000},
    "USA": {"capital": "Washington D.C.", "population": 331000000},
    "Japan": {"capital": "Tokyo", "population": 125000000},
    "France": {"capital": "Paris", "population": 67000000},
    "Brazil": {"capital": "Brasilia", "population": 212000000}
}

with open("countries.json", "w") as f:
    json.dump(countries, f, indent=2)

name = input("Enter a country name: ")

with open("countries.json", "r") as f:
    data = json.load(f)

if name in data:
    info = data[name]
    print(f"Capital: {info['capital']}")
    print(f"Population: {info['population']}")
else:
    print("Country not found.")
