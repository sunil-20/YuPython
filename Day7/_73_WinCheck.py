# Checking if the player have won!
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
# create blank list
display = []
for l in range(len(chosen_word)):
    display += "_"
#condition to start and end the while loop
end_of_game = False
while not end_of_game:
    guess = input("What letter do you guess?\n").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
# condition for ending the while loop after the guessing is completed.
    if "_" not in display:
        end_of_game = True
        print("You win")

