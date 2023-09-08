from art import logo

# define add
def add(n1, n2):
    return n1+n2

#define subtract
def subtract(n1, n2):
    return n1-n2

#define multiply
def multiply(n1,n2):
    return n1*n2

#define divide
def divide(n1,n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    #print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation from the list above: ")  
    should_continue = True
    while should_continue:
        num2 = float(input("What is the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        new_action = input(f"Type 'y' to continue with {answer}, or type 's' to stop or 'r' to restart: ").lower()
        if new_action == 'y':
            num1 = answer
        elif new_action == 's':
            should_continue = False
        else:
            print("Thank you for using calculator app!")
            calculator()
calculator()