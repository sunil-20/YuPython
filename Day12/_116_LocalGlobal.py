
apple_picked = 3

def apple_picking():
  apple_picked = 5
  print(f"Apples picking inside the boundary: {apple_picked}")

apple_picking()
print(f"Apples picking outside the boundary: {apple_picked}")

#Local scope kitchen
def  make_sandwich():
  # local variable in scope of kitchen
  bread = "White pan bread"
  cheese = "Colby Jack cheese"
  mayonnaise = "Hellmans mayonnaise"
  print(f"Making a sandwich with {bread}, {cheese}, and {mayonnaise}.")
make_sandwich()
"""
print(bread) # this will not be printed. Error
"""
# Global scope
apple_tree = "apple tree in the shared garden"
apples_picked = 4
def pick_apples():
  # local variable
  picked_apples = 3
  print(f"Picked {picked_apples} apples from the {apple_tree}.")
  return picked_apples
print(f"Global apple counts: {apples_picked}")
pick_apples()

game_level = 3
def create_enemy():
  enemies = ["Tiger","Lion","Alien"]
  if game_level <5:
    new_enemy = enemies[0]
    print(new_enemy)
    """
print(new_enemy) # not printed because of local scope
"""
create_enemy()