# Write a program that works out whether if a given number is an odd or even number.

number = int(input("Which number do you want to check?"))

type_check = number%2

if type_check ==0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")