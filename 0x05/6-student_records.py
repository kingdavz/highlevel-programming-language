#!/usr/bin/python
"""A module that writes names of students students in a file"""

students = ["john", "jane", "smith", "joy", "mary"] 

with open("records.txt", "w") as file:
    for student in students:
        file.write(student + "\n")


with open("records.txt", "r") as file:
    for idx, student in enumerate(file.readlines()):
        print(f"{idx + 1}: {student}")
