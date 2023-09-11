
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
print(bread) # this will not be printed. Error