#!/usr/bin/python
"""A module that  dumps a json"""
import json

def to_json_string(my_obj):
    """
       a function that return  JSON representatio of an object
       Args:
           my_objs: class object
       Returns:
           JSON representation    
    """
    if my_obj is None:
        return "null"
    return json.dumps(my_obj)

if __name__ == "__main__":
    obj = {
        "school": "Rashotech",
        "Established": 2024
    }
    print(to_json_string(obj))