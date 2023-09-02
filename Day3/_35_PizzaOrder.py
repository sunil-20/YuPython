# order size/type and amount
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1
    
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? L, M or S")
add_pepperoni = input("Do you want to add pepperoni? Y, N")
extra_cheese = input("Do you want extra cheese? Y, N")
final_bill = 0
if size == "L":
    final_bill = 25
elif size == "M":
    final_bill = 20
else:
    final_bill = 15
if add_pepperoni == "Y":
    if size == "S":
        final_bill += 2
    else:
        final_bill += 3
if extra_cheese == "Y":
    final_bill +=1
print(f"Your final bill is: ${final_bill}")
