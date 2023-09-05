#reborg.ca
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