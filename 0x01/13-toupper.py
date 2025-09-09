#!/usr/bin/python
"""A module that converts lowercase letters to uppercase letters"""

def toupper(str):
    result = ""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            result += chr(ord(char) - 32)
        else:
            result += char 
    return result


if __name__ == "__main__":
    string = input("enter a string: ")
    print(toupper(string))
