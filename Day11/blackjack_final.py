import random
from art import logo
def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
# function to return 
def calculate_score(cards):
    """ Return the total from the card on hand."""
    # check for blackjack == 21
    if sum(cards)==21 and len(cards)>2:
        return 0
    if 11 in cards and sum(cards) >21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# comparing user and computer
