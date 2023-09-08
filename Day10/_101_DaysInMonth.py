# leap year
def is_leap(year):
  """ Find the leap year and return True if
  the result is satisfied.
  Check if the days in the month match and return the result and print the number of days
  in the specific month """
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
     return True
  else:
    return False

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year) == True:
    month_days[1]= 29 # February
  return f"{year}, {month_days[month-1]}" # list starts with 0 and input from 1.
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)