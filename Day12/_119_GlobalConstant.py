# you don't want to change the values of constants.
# to differenciate the constants, the naming convention is UPPERCASE.
PI = 3.1416
URL = "https://www.google.com"
TWITTER_HANDLE = "@skvizon"
SHAPE = "Circle"

def calc():
    TWITTER_HANDLE
# from quiz
# In Python there is no block scope.
# Inside a if/else/for/while code block is the same as outside it.
def bar():
    my_variable = 9
    print(f"My first variable: {my_variable}")
 
    if 16 > 9:
      my_variable = 16
 
    print(my_variable)
 
bar()