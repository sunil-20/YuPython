# Blackjack capstone
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# dealing with dealers cards.
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
print(f"Dealers cards: {dealers_cards}")
print(f" Dealers total: {dealers_total}")

# dealing with opponents card.
opponents_cards = []
opponents_total = 0
opponents_draw = True
while opponents_draw:
    if opponents_total < 17:
        new_card_opp = random.choice(cards)
        opponents_cards.append(new_card_opp)
        opponents_total += new_card_opp
    else:
        opponents_draw = False
print( f"Opponents cards: {opponents_cards}")
print(f"Opponents total: {opponents_total}")