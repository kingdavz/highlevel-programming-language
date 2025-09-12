#!/usr/bin/python
"""A module that implements a guessing game"""
import random

trial = 3
while trial != 0:
    num = random.randint(1, 5)
    guess = int(input("guess a number between 1 and 5: "))
    if guess == num:
        print("you win")
        break
    else:
        print("try again")
    trial -= 1
    