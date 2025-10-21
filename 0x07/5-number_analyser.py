#!/usr/bin/python
"""A module that analyse numbers"""


numbers = []


for I in range(10):
    Num = int(input("Enter number {i+1}: "))
    numbers.append(Num)


evens = [n for n in numbers if n % 2 == 0]
odds = [n for n in numbers if n % 2 != 0]


print("\nEven numbers:", evens)
print("Odd numbers: ", odds)
print("Sum of all numbers: ", sum(numbers))
print("Largest number: ", max(numbers))
print("Smallest number: ", min(numbers))

