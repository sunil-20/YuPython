# Adding Even Numbers 1 to 100 including 1

total = 0
for number in range(1,101):
    if number == 1 or number % 2 ==0:
        total+= number
print(total)

# way 2 adding even 1 to 100
total2 = 0
for number2 in range (2, 101, 2):
    total2 += number2
print(total2)

