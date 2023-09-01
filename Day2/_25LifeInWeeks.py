# Your life in a week

# ask for age of the person and store in a variable named age and change type to int.
age = int(input("What is your current age? "))
years_remaining = 90 - age

days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining  * 12

print( f" You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months, and {years_remaining} years left.")
