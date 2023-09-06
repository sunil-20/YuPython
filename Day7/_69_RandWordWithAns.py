import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
guess = input("What letter do you guess?\n").lower()
# to check every occurance you have to use for loop
# if else will check just the first occurance.
for letter in chosen_word:
    if letter == guess:
        print("Yes")
    else:
        print("No")