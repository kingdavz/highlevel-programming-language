#!/usr/bin/python
"""A module that writes an object to a text file"""
import json

def save_to_json_file(my_obj, filename):
    """
       A function that writes an object to a text file
       Args:
           my_obj: python object datastructure
           filename: name of the file to write inside
       Returns:
           number of characters written to the file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(json.dumps(my_obj))
    
if __name__ == "__main__":
    obj = {
        "name": "Rashotech",
        "Established": 2024,
        "slogan": "Dream it, let's achieve it"
    }
    save_to_json_file(obj, "example.json")
