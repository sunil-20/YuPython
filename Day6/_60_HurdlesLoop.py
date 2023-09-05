#reborg.ca
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def u_turn():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while at_goal() == False:
   u_turn()
# or second option
while not at_goal():
  u_turn()

  ## second hurdle jump

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
   move()
   turn_left()
   move()
   turn_right()
   move()
   turn_right()
   move()
   turn_left()

for step in range(6):
   jump()

# method used by me
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
        """