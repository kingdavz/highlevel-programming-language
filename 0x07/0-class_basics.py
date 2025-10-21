#!/usr/bin/python
"""A module that creates a class"""

class Car:
    make = "Toyota"
    model = "Camery"
    year = 2008

if __name__ =="__main__":
    car = Car()
    print(car.make)
    print(car.model)
    print(car.year)
    print(type(car))