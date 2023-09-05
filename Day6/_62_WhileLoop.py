#Reborg example
# while loop is used to repeat something until the condition is false.

def turn_right():
    for x in range(3):
        turn_left()
    move()
while not at_goal():
    if right_is_clear():
        turn_right()
    elif is_facing_north() and front_is_clear():
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
            