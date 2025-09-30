#!/usr/bin/python
"A module that handles set operations"

python_students = {"Alice", "Bob", "Charlie"}
java_students = {"Charlie", "Diana", "Ethan"}


both = python_students & java_students  


only_python = python_students - java_students  
only_java = java_students - python_students 


results = {
    "both": both,
    "only_python": only_python,
    "only_java": only_java
}


print("Results:")
for category, students in results.items():
    print(f"{category}: {students}")
