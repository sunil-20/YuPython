# Nested example with rollercoaster ride
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

if height >=120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age <= 12:
        print("You have to pay 5 dollars.")
    elif age >12 and age <=18:
        print("You have to pay 7 dollars.")
    else:
        print("You have to pay 12 dollars.")
else:
    print("You are not tall enough to ride the rollercoaster.")