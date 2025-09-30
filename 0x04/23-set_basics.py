#!/usr/bin/python
"A module that carries out set operations"

num = {1, 2, 3, 4, 5}

user_input = int(input("Enter a number: "))

if user_input in num:
    num.remove(user_input)
    print(f"{user_input} was in  the set and has been removed.")
else:
    num.add(user_input)
    print(f"{user_input} was not in the set and has been added.")

    print("Final set: ", num)
