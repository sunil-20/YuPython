# BMI Calculator 2.0

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

BMI = round(float(weight)/float(height)**2)

if BMI <=18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clicinically obese.")
