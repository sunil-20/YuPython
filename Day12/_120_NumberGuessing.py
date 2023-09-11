# Number Guessing game
import random
from art import logo
print(logo)
def guess_me():
        print("Welcome to the number guessing game")
        print("I am thinking a number between 1 and 50")
        number = random.randint(1, 50) # a and b inclusive
        #print(f"The guessed number is: {number}.")
        total_try = 0
        if input("Which level do you want to play? 'easy' or 'hard'? ").lower()=='easy':
            total_try += 10
        else:
            total_try += 5
        print(total_try)
        game_stop = False
        while not game_stop:
            guess = int(input("What number do you guess?: "))
            total_try-=1
            if guess > number:
                print(f"You guessed too high. \nYou have {total_try} attempts remaining.")
            elif guess == number:
                print(f"You guessed corret!")
                game_stop = True
            else:
                print(f"You guessed too low. \nYou have {total_try} attempts remaining.")

            # last attempt condition
            if total_try ==0 and guess != number:
                print("You run out of guesses! You lose!")
                game_stop = True
            elif total_try == 0 and guess == number:
                 print("You ran out of the guesses but you won at the very end!")
                 game_stop = True
guess_me()