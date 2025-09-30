#!/usr/bin/python
"A module that ask user to guess numbers"

import random

number_to_guess = random.randint(1,20)

while True:
    guess = int(input("guess a number etween 1 and 20: "))

    if guess < number_to_guess:
        print("too low")
    elif guess > number_to_guess:
        print("too high")
    else:
        print("correct! you guessed the number.")
        break