#!/usr/bin/python
"""A module that uses import"""
import sys
from calc import add, sub, div, mul, mod, exp
from sys import argv, exit

operator = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
    "%": mod,
    "**": exp
}

if __name__ == "__main__":
    if len(argv) != 4:
        print("invalid number of arguments")
        exit(1)
    num1 = int(argv[1])
    num2 = int(argv[3])
    op = argv[2]

    for key in operator.items():
        if op == key:
            print((num1,num2))
            exit(0)
    print("unknown operator. available opertors: +, -, *, /, %, **")
    exit(1)