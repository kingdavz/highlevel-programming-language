#!/usr/bin/python

"""A module that return JSON to string"""
import json


def from_json_string(my_str):
    """
       A function that convert json to string
       Args:
           my_str: json notation
       Returns:
           an object represented by a JSON string
    """
    return json.loads(my_str)

if __name__ =="__main__":
    my_val = '{ "student":{"firstname": "chukwuma","lastname": "okonkwo", "age": 25,"gender": "male"}}'
    print(from_json_string(my_val))

