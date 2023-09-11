# Number Guessing game
import random
from art import logo
print(logo)
total_try = ""
if 


def guess_me():
    print("Welcome to the number guessing game")
    print("I am thinking a number between 1 and 50")
    number = random.randint(1, 50) # a and b inclusive
    print(f"The guessed number is: {number}.")
    guess = int(input("What number do you guess?: "))

guess_me()