#!/usr/bin/python
"""A module that changes the size of a string"""

def length(text):
    size = 0
    for _ in text:
        size += 1
    return size




if __name__ == "__main__":
    message = input("Enter your message: ")
    print(length(message))
    print(len(message))
