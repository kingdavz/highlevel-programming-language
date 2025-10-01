#!/usr/bin/python
"""A main entry to the program"""
import sys

func = __import__("0-import")

operator = {
    "+": func.add,
    "-": func.sub,
    "*": func.mul,
    "/": func.div,
    "%": func.mod,
    "**": func.exp
}

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("invalid number of arguments")
        sys.exit(1)
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[3])
    op = sys.argv[2]

    for key in operator.items():
        if op == key:
            print(func(num1,num2))
            sys.exit(0)
    print("unknown operator. available opertors: +, -, *, /, %, **")
    sys.exit(1)