from data import resources, MENU

total_fund_available = 0


def is_resource_sufficient(order_ingredients):
    """ Return True if order can be placed if not False because of insufficient resources."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f" Sorry {item} is not sufficient to order coffee.")
            return False
    return True


def insert_coins():
    """ Returns the total value of inserted coins."""
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total_dollar = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total_dollar


def is_transaction_successful(fund_available, drink_cost):
    """ Return True when payment is processed successfully. False if fund is insufficient."""
    if fund_available >= drink_cost:
        change = round(fund_available - drink_cost, 2)
        print(f"Here is your ${change} in change.")
        global total_fund_available
        total_fund_available += drink_cost
        return True
    else:
        print("No enough fund. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """ Deduct the required ingredients from the source."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


is_on = True
while is_on:
    choice = input("What would you like to order ? espresso/latte/cappuccino:").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${total_fund_available}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = insert_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
