#!/usr/bin/python
"""A module that selects odd numbers and arranges them in descending order"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = []
for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)

odd_numbers.sort(reverse=True)
print("odd numbers in descending order: ", odd_numbers)
