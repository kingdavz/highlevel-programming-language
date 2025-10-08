#!/usr/bin/python
"""A module that can open a file"""

def filereader(filename):
    """A function that reads a file"""
    file = open(filename, "r")
    for line in file:
        print(line, end="")
    file.close()




if __name__ == "__main__":
    filereader("main.py")

