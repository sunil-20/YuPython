# Number Guessing game
import random
from art import logo
print(logo)
game_stop = False
while not game_stop:

    def guess_me():
            print("Welcome to the number guessing game")
            print("I am thinking a number between 1 and 50")
            number = random.randint(1, 50) # a and b inclusive
            print(f"The guessed number is: {number}.")
            total_try = 0
            if input("Which level do you want to play? 'easy' or 'hard'? ").lower()=='easy':
                total_try += 10
            else:
                total_try += 5
            print(total_try)
            guess = int(input("What number do you guess?: "))
            for i in range(1,total_try+1):
                total_try-=1
                if guess > number:
                    print(f"You guessed too high. \n You have {total_try} attempts remaining.")
                elif guess == number:
                    print(f"You guessed corret!")
                else:
                    print(f"You guessed too low. \n You have {total_try} remaining.")
            if total_try ==0:
                game_stop = True
    guess_me()
#guess_me()