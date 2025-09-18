#!/usr/bin/python
"""A module that requests the name of students and stores  it in a list"""

def get_student_names():
    students_names = []

    num = input("how many students do you want to enter? ")
    num = int(num)

    for i in range(num):
        name = input("Enter the name of students: ")
        students_names.append(name)
        return students_names
    
names = get_student_names()
print("student names: ")
print(names)