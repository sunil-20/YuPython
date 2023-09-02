# Add a condition with photo 
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))
bill = 0
if height >=120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age <= 12:
        bill = 5
        print("Child tickets are 5 dollars.")
    elif age >12 and age <=18:
        bill = 7
        print("Youth tickets are 7 dollars.")
    else:
        bill = 12
        print("Adult tickets are 12 dollars.")
    add_photo = input ("Do you want to take photo? Y or N.")
    if add_photo == "Y":
        bill+=3
        print(f"Your final bill is ${bill}.")
    else:   
        print(f"Your final bill is ${bill}.")
else:
    print("You are not tall enough to ride the rollercoaster.")