
# number = int(input("Which number do you want to check?"))
# # assignment operator(=) used instead of comparision(==) operator.
# if number % 2 == 0:
#   print("This is an even number.")
# else:
#   print("This is an odd number.")
  
# Debugging leap year

year = int(input("Which year do you want to check?"))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
  