# Functions with Outputs Lect 99
"""
def my_function(something): # something is parameter
    #Do this with something
    #Then do this
    #Finally do this

#call the fx
my_function(123) # 123 is argument
    
"""

# fx with outputs
f_name = input("What is your name?\n")
l_name = input("What is your last name?\n")
def format_name(f_name, l_name):
    final_name = f_name.title() +" "+ l_name.title()
    print(final_name)
format_name(f_name= f_name, l_name= l_name)
# code changes to return
f_name = input("What is your name?\n")
l_name = input("What is your last name?\n")
def format_name(f_name, l_name):
    return f_name.title() +" "+ l_name.title()

print(format_name(f_name= f_name, l_name= l_name))