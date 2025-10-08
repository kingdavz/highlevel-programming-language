#!/usv/bin/python
"""A module that can read a csv file"""
import csv

def read_csv(filename):
    """A function that reads a csv file"""
    with open(filename) as file:
        lines = csv.reader(file, delimiter=",")
        for line in lines:
           print(' '.join(line))


if __name__ =="__main__":
    read_csv("example.csv")
