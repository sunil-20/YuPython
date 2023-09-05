# def turn_right():
    for x in range(3):
        turn_left()
    #move()
while not at_goal():
    if is_facing_north() and front_is_clear():
        move()
    elif is_facing_north() and wall_in_front():
        turn_right()
        if front_is_clear():
            move()
        else:
            turn_right()
    elif wall_in_front():
       turn_left()
        
    elif front_is_clear():
        move()
    else:
        turn_left()
    