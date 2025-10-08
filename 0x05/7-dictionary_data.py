#!/usr/bin/python
"""A module that shows dictionary data"""

subjects = {}

if __name__ == "__main__":
    num =int(input("Enter a number of subject: "))

    with open("scores.txt", "w") as file:
        file.write("")

    while num > 0:
        subject = input("Enter subject name: ")
        score = int(input("Enter subject score: "))
        subjects.update({subject: score})
        num -= 1

    with open("scores.txt", "a+") as f:
        for subject, score in subjects.items():
            f.write(f"{subject}: {score} "+"\n")

    with open("scores.txt", "r") as file:
        for line in file.readlines():
            subject, score = line.split(": ")
            if int(score) > 70:
                print(f"{subject} : {score}")
        
