# leap year
def is_leap(year):
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
  """
  Take the year and month as input and output the year and the number of days in
  the month. Changes February to 29 if it is a leap year.

  """
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year) == True:
    month_days[1]= 29 # February
  return f"{year}, {month_days[month-1]}" # list starts with 0 and input from 1.
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)