## Debugging
## Leap year explanation and code.
Leap years are years that have an extra day, February 29th, to keep our calendar year synchronized with the Earth's revolutions around the Sun. In the Gregorian calendar, which is the most widely used calendar system today, leap years follow these rules:

1. A year is a leap year if it is divisible by 4.

2. However, years divisible by 100 are not leap years, unless they are also divisible by 400.

Following these rules, here are some examples of leap years and non-leap years:

**Leap Years:**
- 2024
- 2000
- 1996

**Non-Leap Years:**
- 2022
- 1900
- 1800

Explanation for non-leap years like 1900: Although they are divisible by 4, they are not leap years because they are also divisible by 100 and not by 400.

You can use these rules to determine if a particular year is a leap year in Python. Here's a simple Python function to check if a year is a leap year:

```python
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Example usage:
year = 2024
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
```

This function checks the conditions mentioned earlier to determine if a year is a leap year and returns `True` or `False` accordingly.