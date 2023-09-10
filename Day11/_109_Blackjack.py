# Blackjack capstone
import random
from art import logo
print(logo)
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

# Dealer's additional drawing
if dealers_total > 21:
    print("Dealer Busted.")
elif dealers_total == 21:
    print("Dealer's Blackjack")
else:
    shall_draw = input("Do you want to draw more cards? y or n").lower()
    if shall_draw == 'y':
        new_card_re1 = random.choice(cards)
        dealers_cards.append(new_card_re1)
        dealers_total += new_card_re1
        print(f"Dealers cards: {dealers_cards}")
        print(f" Dealers total: {dealers_total}")
    else:
        print(f"Dealers cards: {dealers_cards}")
        print(f" Dealers total: {dealers_total}")

# Opponent's additional drawing
if opponents_total > 21:
    print("Opponent Busted!")
elif opponents_total == 21:
    print("Opponent's Blackjack")
else:
    shall_draw_opp = input("Do you want to draw more cards? y or n").lower()
    if shall_draw_opp == 'y':
        new_card_opp_re1 = random.choice(cards)
        opponents_cards.append(new_card_opp_re1)
        opponents_total += new_card_opp_re1
        print(f"Opponents cards: {opponents_cards}")
        print(f"Opponents total: {opponents_total}")
    else:
        print(f"Opponents cards: {opponents_cards}")
        print(f"Opponents total: {opponents_total}")


