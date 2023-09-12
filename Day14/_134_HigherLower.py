import random
import art
import game_data
print(art.logo)

def high_low():
    compare_a = random.choice(game_data.data)
    game_over = False
    score = 0
    while not game_over:
        compare_a = compare_a
        compare_b = random.choice(game_data.data)
        while compare_a == compare_b:
            compare_b = random.choice(game_data.data)

        followers_a = compare_a['follower_count']
        print(f"Compare A: {compare_a['name']}, {compare_a['description']}, from {compare_a['country']}")
       
        print(art.vs)
        
        followers_b = compare_b['follower_count']
        print(f"Against B: {compare_b['name']}, {compare_b['description']}, from {compare_b['country']}")
        # user input for  a or b
        a_or_b = input("Who has more followers? 'A' or 'B': ").lower()
        if a_or_b == 'a' and followers_a > followers_b:
            score +=1
            print(f"Your guessed right, your score is: {score}")
            
        elif a_or_b == 'b' and followers_b > followers_a:
            score +=1
            compare_a = compare_b
            print(f"Your guessed right, your score is: {score}")
        else:
            print(f"You guessed wrong!, your score is: {score}.")
            game_over = True

high_low()