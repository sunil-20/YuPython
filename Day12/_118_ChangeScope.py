# creating a new variable that has a local scope
food = "Rice"
def new_food():
    food = ""
    food = "Burger"
    #local scope
    print(f"I will be eating {food}.")
new_food()
#global scope
print(f"I will rather eat {food}.")
############################################################################
# modification to change the global var food.

food = "Rice"
def new_food():
    global food
    food = "Burger"
    #local scope
    print(f"I will be eating {food}.")
new_food()
#global scope it should print the same as local
print(f"I will rather eat {food}.")
