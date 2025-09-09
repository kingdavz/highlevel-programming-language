#!/usr/bin/python
"""A program that can play the game of rock paper scissors"""
import random

def get_user_choice():
    choice = input("enter your choice(rock, paper, or sccisors)").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("invalid choice. try again.")
        choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    return choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])
    

def determine_winner(user, computer):
    if user == computer :
        return "it's a tie"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper') :
        return "you win!"
    else:
        return "you lose!"

def play_game():
    print("=== rock paper scissors ===")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nresult: {user_choice}")
    print(f"computer chose: {computer_choice}")  

    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()


