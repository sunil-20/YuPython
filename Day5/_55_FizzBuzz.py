# 3 & 5 == FIZZBUZZ, 3 == FIZZ, 5 == Buzz
# be careful with result overlap, as 3 and 5 togetether and separated.

#check a single number as user's input
number = int(input("What number do you choose?"))
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)

# check numbers from 1 to 100
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)