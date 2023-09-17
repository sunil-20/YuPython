# Coffee machine codes
from data import resources, MENU, coin

report_ingredients = input("Do you want to view the status of the ingredients? 'yes' or 'no'").lower()
if report_ingredients == "yes":
    print(f"Water: {resources['water']},\nMilk: {resources['milk']},\nCoffee: {resources['coffee']}")

coffee_type = input("What would you like?(espresso/latte/cappuccino): ").lower()
coffee_price = 0
if coffee_type == "espresso":
    espresso_price = MENU['espresso']['cost']
    coffee_price += espresso_price
elif coffee_type == "latte":
    latte_price = MENU['latte']['cost']
    coffee_price += latte_price
elif coffee_type == "cappuccino":
    cappuccino_price = MENU['cappuccino']['cost']
    coffee_price += cappuccino_price
print(f"Price of {coffee_type.title()} is: {coffee_price}")

total_dollar_fund = 0
change = 0
rebrew_coffee = True
while rebrew_coffee:

    def coin_insert():
        print("Please insert coins.")
        global total_dollar_fund
        global rebrew_coffee
        global change
        if total_dollar_fund < coffee_price:

            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            total_dollar = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
            total_dollar_fund = total_dollar

        change = round(total_dollar_fund - coffee_price, 2)
        if total_dollar_fund < coffee_price:
            print("You have insufficient fund to brew the coffee!")
            insert_coin = input("Do you want to insert more coins? 'yes' or 'no'.")
            if insert_coin == "yes":
                coin_insert()
            else:
                rebrew_coffee = False
        else:
            print(f"You have sufficient fund to brew {coffee_type}. Here is your change: {change}.\n Enjoy the coffee!")

            rebrew = input("Yes or No").lower()
            if rebrew == "no":
                rebrew_coffee = False
            else:
                print(f"Fund left: {change}")
                total_dollar_fund = change
                rebrew_coffee = True

    coin_insert()
