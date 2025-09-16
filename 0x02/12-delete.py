#!/usr/bin/python
"""A module that can remove characters in a string"""

def remove_character(sentence, char_to_remove):
    return sentence.replace(char_to_remove, "")


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    char_to_remove = input("enter the character to remove: ")
if len(char_to_remove) != 1:
    print("Please enter only one character.")
else:
    new_sentence = remove_character(sentence, char_to_remove)
    print("updated sentence:", new_sentence)
