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
def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return " Game over >21"
    
    if user_score == computer_score:
        return "Draw"
    elif computer_score ==0:
        return " You lose, opponent got blackjack"
    elif user_score >21:
        return("You lose >21")
    elif computer_score > 21:
        return " You win opponent"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"
    
def play_game():

    print(logo)

    user_cards = []
    computer_cards = []
    game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your cards: {user_cards}, current score")