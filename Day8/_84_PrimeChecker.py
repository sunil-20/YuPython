# function checking a prime number.


def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number_to_check % i == 0:
            is_prime = False
    if is_prime == False:
        print(f" The number {number_to_check} is not a prime number")
    else:
        print(f"The number {number_to_check} is a prime number.")

number_to_check = int(input("Which number do you want to check?\n"))
prime_checker(number = number_to_check)

