import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
guess = input("What letter do you guess?\n").lower()

if guess in chosen_word:
    print("Yes")
else:
    print("No")