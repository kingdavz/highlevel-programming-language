#!/usr/bin/python
"""A module that creates a class Person"""

class person:
    name = "John doe"
    age  = 25
    height = "6ft"
    hobbies = "playing music and games"


if __name__ =="__main__":
    person1 = person()
    print(person1.name)
    print(person1.age)
    print(person1.height)
    print(person1.hobbies)
    print(type(person1))