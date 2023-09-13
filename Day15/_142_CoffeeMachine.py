# Coffee machine codes
from data import resources, MENU, coin

report_ingredients = input("Do you want to view the status of the ingredients? 'yes' or 'no'").lower()
if report_ingredients == "yes":
    print(f"Water: {resources['water']},\nMilk: {resources['milk']},\nCoffee: {resources['coffee']}")

coffee_type = input("What would you like?(espresso/latte/cappuccino): ").lower()
price = 0
if coffee_type == "espresso":
    espresso_price = MENU['espresso']['cost']
    price += espresso_price
elif coffee_type == "latte":
    latte_price = MENU['latte']['cost']
    price += latte_price
elif coffee_type == "cappuccino":
    cappuccino_price = MENU['cappuccino']['cost']
    price += cappuccino_price
print(f"Price of {coffee_type.title()} is: {price}")


# def coin_insert(q, d, n, p):
#     total_dollar = q * 0.25 + d * 0.10 + n * 0.05 + p * 0.01
#     return total_dollar
#
#
# print("Please insert coins.")
# quarters = int(input("How many quarters?: "))
# dimes = int(input("How many dimes?: "))
# nickles = int(input("How many nickles?: "))
# pennies = int(input("How many pennies?: "))
#
# total = coin_insert(q=quarters, d=dimes, n=nickles, p=pennies)
#
#
# print(total)
# print(coffee_type)
