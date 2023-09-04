# for loop and the range function.
"""for number in range(a,b):
        print(number)

"""
# range includes 1 to 9 if specified(1,10)
for number in range(1,11):
    print(number)

# with steps
for number in range (1, 11, 2):
    print(number)
# add
total = 0
for number in range(1, 101):
    total += number
print(total)