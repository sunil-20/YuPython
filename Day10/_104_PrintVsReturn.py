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

num1 = int(input("What's the first number?: "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the list above: ")  
num2 = int(input("What is the second number?: "))
calculation_function = operations[operation_symbol]

first_answer = calculation_function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {first_answer}")

# pick another operation so you can use the previous operation as input using return
operation_symbol = input("Pick an operation from the list above: ")  
num3 = int(input("What is the second number?: "))
calculation_function = operations[operation_symbol]
second_answer = calculation_function(first_answer,num3)
print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")