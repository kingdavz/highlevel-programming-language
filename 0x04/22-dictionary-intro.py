#!/usr/bin/python
"A module that carries out dictionary operations"

person = {
    "name": "john",
    "age": 23,
    "city": "lagos"
}

new_city = input("Enter new city: ")

person["city"] = new_city
print("Updated dictionary:")
print(person)
