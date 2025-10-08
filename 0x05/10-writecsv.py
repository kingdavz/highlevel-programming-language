#!/usr/in/python
"""A module that creates and writes into a csv file"""
import csv

def write_csv(filename, data):
    with open(filename, "a+", newline="")as file:
        writer = csv.writer(file)
        writer.writerow(data)



if __name__ =="__main__":
    write_csv(
        "employee.csv",
        ['S/N', 'Name', 'Age', 'Salary'])