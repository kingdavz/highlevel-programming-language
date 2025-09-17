#!/usr/bin/python
"""A module that copies a list"""

letters = ['a', 'b', 'c', 'd', 'e']
letter_copy = letters.copy()

print(letter_copy)
letters[1] = "k"
print(f"copied list {letter_copy}")
print(f"original list {letters}")
