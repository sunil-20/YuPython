# Rock Paper Scissors game
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
computer = random.randint(0,2)
# computer's hand
print("Computer hand.")
if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
else:
    print(scissors)

# users hand
user = int(input("What number do you want to choose? 0, 1 or 2:"))
print("Your hand")

if  user == 0:
    print(rock)
elif user == 1:
    print(paper)
else:
    print(scissors)

# check invalid number first
if user >= 3 and user <0:
    print("Invalid number provided.")
elif user == computer:
    print("You have a tie.")
elif computer ==0 and user ==2:
    print("You lose!")
elif computer == 2 and user ==1:
    print("You lose!")
elif computer == 1 and user == 0:
    print("You lose")
else:
    print("You win!! Congratulations!!")