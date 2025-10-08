#!/usr/bin/python
"""A module that deletes a file that exist"""
import os


def delete(filename):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        raise FileExistsError("file doesn't exist")
    return f"{filename} is deleted successfully"



if __name__ =="__main__":
    filename = input("Enter the filename to be deleted: ")
    if filename != "" or filename is not None:
        delete(filename)
    else:
        print("file cannot be empty")
        

