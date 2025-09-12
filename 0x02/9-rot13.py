#!/usr/bin/python
"""A module that solves rot13"""

def rot13(text):
    result =""

    for char in text:
        if char.islower():
            new_char = chr((ord(char) - ord ('a')+ 13) % 26 + ord('a'))
            result += new_char
        elif char.isupper():
            new_char = chr ((ord(char) - ord('A') + 13) % 26 + ord('A'))
            result += new_char
        else:
            result += char

    return result

message = input("Enter your message: ")
rot13_message = rot13(message)
print("ROT13 output:", rot13_message)