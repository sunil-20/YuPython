import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
display = []
for letter in range(len(chosen_word)):
    display += "_"
print(display)
guess = input("What letter do you guess?\n").lower()

for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = guess
    else:
        display[position] = "_"
print(display)

