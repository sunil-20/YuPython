# if a given year is a leap year?

year = int(input("What year do you want to check?"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year 400 yes")
        else:
            print("Not leap 400 no")
    else:
        print( "Not leap year 100 no")   
else:
    print("Not leap year 4 no")

