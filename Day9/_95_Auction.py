import art
import os
import time
delay_seconds = 5
bidders = {}
print(art.logo)
auction = True
while auction:
    name = input("What is your name?\n")
    bid = float(input("What is you bid amount?\n"))
    single_bidder = {}
    single_bidder[name] = bid
    bidders.update(single_bidder)
    add_bidders = input("Do you want to add bidders Y or N?\n").lower()
    if add_bidders == 'n':
        auction = False
        # Extract tuples for the highest bid amount
        highest_bid = max(bidders.items(), key = lambda x:x[1])

        # separate the tuple to key and value pair
        max_key, max_value = highest_bid
        print(f" The bidder with the largest value is '{max_key} with value of '{max_value}")






# clear terminal screen
# time.sleep(delay_seconds)
# os.system("cls")