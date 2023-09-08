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
    num1 = int(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation from the list above: ")  
    num2 = int(input("What is the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    add_numbers = input("Do you want to add more numbers? yes or no/n").lower()
    while add_numbers == "yes":
    # pick another operation so you can use the previous operation as input using return
        operation_symbol = input("Pick an operation from the list above: ")  
        answer_in = answer
        num3 = int(input("What is the number?: "))
        calculation_function = operations[operation_symbol]
        answer_final = calculation_function(answer_in, num3)
        print(f"{answer_in} {operation_symbol} {num3} = {answer_final}")
        add_numbers = input("Do you want to add more numbers? yes or no/n").lower()
        answer_in = answer_final

    restart = input("Do you want another calculation to perform? yes or no/n")
    if restart == "yes":
        calculator()
        print("Thank you for using calculator app!")
