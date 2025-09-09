#!/usr/bin/python
""""A module that converts uppercase letters to lowercase letters"""

def tolower(str):
    result = ""
    for char in str:
        if ord(char) >= 65 and ord(char) <= 90:
            result += chr(ord(char) + 32)
        else:
            result += char
    return result
        



if __name__ == "__main__":
    string = input("enter a string: ")
    print(tolower(string))

        