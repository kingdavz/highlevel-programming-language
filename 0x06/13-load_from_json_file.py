#!/usr/bin/python
"""A module that creates an object"""
import json

def load_from_json(filename):
    """
       A function that creates an object from a JSON file
       Args:
           filename: file that contains JSON
    """
    with open(filename) as f:
        obj = json.load(f)
        return obj
    
if __name__ == "__main__":
    obj = load_from_json("example.json")
    print(obj)