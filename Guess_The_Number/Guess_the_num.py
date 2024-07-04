# play_game() : To start the game and to take user input keeping track of total attempts remaining
# compare() : To compare user input with actual number
import random
import os

def compare(attempts, actual_number):
    chosen_number = int(input(f"You have {attempts} attempts remaining to guess the number.\nMake a guess: "))
    if chosen_number > actual_number:
        print("Too high!\nGuess again.\n")
    elif chosen_number < actual_number:
        print("Too low!\nGuess again.\n")
    else:
        print(f"You got it! The answer is {actual_number}\n")
        return "guessed"

def play_game():
    # Take user_input to decide number of chances
    valid = True
    while valid:
        user_input = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if user_input == "easy":
            attempts_remaining = 10
            valid = False
        elif user_input == "hard":
            attempts_remaining = 5
            valid = False
        else:
            print("Invalid Input! Try again") 
            
    print()
    number = random.randint(1, 101)
    while attempts_remaining:
        result = compare(attempts_remaining, number)
        attempts_remaining -= 1
        if result == "guessed":
            break
        if attempts_remaining == 0:
            print(f"Oops! You've used up all your chances.\nThe actual number is {number}.")

from art import logo

print(logo)
print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 to 100.")
play_game()

wanna_play_again = True
while wanna_play_again:
    user_choice = input("Hope you had fun!\nWanna play again?: (y/n)")
    if user_choice == "y":
        os.system("cls")
        play_game()
    else:
        wanna_play_again = False
