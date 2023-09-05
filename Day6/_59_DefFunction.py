# defining a function
# print() is a function, len() is a function 
# we use def to create our own function
def my_function(a,b):
    total = a + b
    print(total)
# call the function 
my_function(2, 3)

#Reborg https://reeborg.ca/
def turn_right():
    for x in range(3):
        turn_left()

# creating a square
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()

