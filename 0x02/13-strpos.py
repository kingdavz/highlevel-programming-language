#!/usr/bin/python
"""A madule that can check the position of a string"""

def find_positon(sentence, search_string):
    position = sentence.find(search_string)
    return position



if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    search_string = input("Enter the string to find: ")
    positon = find_positon(sentence, search_string)
    
if positon != -1:
    print("The string was found at position: ", positon)
else:
    print("The string was not found in the sentence.")