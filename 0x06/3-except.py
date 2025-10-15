#!/usr/bin/python
"""A module that performs divisions"""

try: 
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter the second number: "))
    result =num1 / num2
except ValueError:
    print("Invalid datatype")
except ZeroDivisionError:
    print("cannot divide by zero")
except Exception as e:
    print(e)
else:
    print(f"The result of {num1} / {num2} is {result}")
finally:
    print("Execution completed")