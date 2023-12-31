#Improve UI
import random
# another way of importing // this is redundant but just to note.
from stages import logo, stages_fig
import hangman_words

print(logo)
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
lives = 6
print(chosen_word)
# create blank list
display = []
for l in range(word_length):
    display += "_"
#condition to start and end the while loop
end_of_game = False
while not end_of_game:
    guess = input("What letter do you guess?\n").lower()
# prompt for repeated guess.
    if guess in display:
        print(f"You've already guessed {guess}.")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. So, you lose a life.")
        lives-=1
        print(f"Lives remaining: {lives}")
        if lives<1:
            end_of_game = True
            print("You lose!")
            print(f"The word was: {chosen_word}")

    # print the word after joining from the list
    print(f"{''.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")
        print(f"The word was: {''.join(display)}")
    print(stages_fig[lives])
