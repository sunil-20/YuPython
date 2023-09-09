# Blackjack capstone
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#dealers_draw = random.choice(cards)
dealers_cards = []
dealers_total = 0
dealers_draw = True
while dealers_draw:
    if dealers_total <17:
        new_card = random.choice(cards)
        dealers_cards.append(new_card)
        dealers_total += new_card
    else:
        dealers_draw = False
print(dealers_cards)
print(dealers_total)
#computer_card = random.choice(cards)