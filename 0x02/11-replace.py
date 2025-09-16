#!/usr/bin/python
"""A module that replaces characters in a string"""

def replace(text, old_char, new_char):
    new_message = ""
    for char in text.split():
        if char == old_char:
            new_message += new_char + " "
        else:
            new_message += char + " "
    return new_message



if __name__ == "__main__":
    message = input("Enter your message: ")
    old_text = input("What do you want to replace: ")
    new_text = input("Enter new text: ")


    new_message = replace(message, old_text, new_text)
    print(new_message)


            