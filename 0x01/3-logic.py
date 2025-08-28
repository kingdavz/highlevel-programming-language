#!/usr/bin/python
"""A module that handles if statements and calculations"""
score = int(input("Enter your score:"))
if score  >= 90 and score <= 100:
    print("you have an A grade")
elif score >= 80 and score < 90:
    print( "you have a B grade")
elif score >= 70 and score < 80:
    print("you have a C grade")
elif score >= 60 and score < 70:
    print("you have a D grade")
elif score >=0 and score < 60:
    print("you have a F grade")
else:
    print("invalid score")
