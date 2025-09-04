#!/usr/bin/python
"""A module that makes use of switch functions"""

def add (a,b):
    return a+b

def sub (a,b):
    return a-b

def multiply (a,b):
    return a*b

def divide (a,b):
    return a/b

def mod (a,b):
   return a%b
   
def expo (a,b):
    return a**b

if __name__ =="__main__":
    opt =int(input(" enter 1-add,2-sub,3-multiply,4-divide,5-mod,6-expo: "))
    num1=int(input(" enter the first number: " ))
    num2=int(input(" enter the second number: "))

if opt==1:
    print(add(num1,num2))

elif opt==2:
    print(sub(num1,num2))

elif opt==3:
    print(multiply(num1,num2))

elif opt==4:
    print(divide(num1,num2))

elif opt==5:
    print(mod(num1,num2))

elif opt==6:
    print(expo(num1,num2))

else:
    print("invalid input")                
