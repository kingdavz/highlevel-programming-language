#!/usr/bin/python
"""A module that can append to a file"""

def appendfile(filename, content):
    """A function that appends content to a file"""
    with open(filename, "a") as file:
        file.write(content)



if __name__ == "__main__":
    appendfile("example.txt",
               " and JavaScript programing is amazing")