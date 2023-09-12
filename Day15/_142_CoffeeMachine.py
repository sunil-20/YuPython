
# Coffee machine codes
from data import resources, MENU, coin

report_ingredients = input("Do you want to view the status of the ingredients? 'yes' or 'no'").lower()
if report_ingredients == "yes":

    print(f"Water: {resources['water']},\nMilk: {resources['milk']},\nCoffee: {resources['coffee']}")

coffee_type = input("What would you like?(espresso/latte/cappuccino): ").lower()

 def coin_insert(q, d, n, p):
     total = q+d+n+p
     return total

 print("Please insert coins.")
 quarters = int(input("How many quarters?: "))
 dimes = int(input("How many dimes?: "))
 coin_insert(q, d, n, p)
 print(total)

print(coffee_type)
