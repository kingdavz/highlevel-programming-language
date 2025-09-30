#!/usr/bin/python
"A module that carries out tuple operations"

subjects = ("maths","chemistry","english","physics","biology")

subject_list = list(subjects)
subject_list.append("history")

updated_subjects = tuple(subject_list)

print("Updated subjects tuple: ")
print(updated_subjects)