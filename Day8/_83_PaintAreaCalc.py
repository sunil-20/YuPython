# Paint area calculator
import math
wall_height = float(input("What is the height of the wall?\n"))
wall_width = float(input("What is the width of the wall?\n"))
coverage = 5

def paint_calculator(wall_height, wall_width, coverage):
    number_of_cans = (wall_height* wall_width)/ coverage
    # use ceil to round to the whole cane needed. This will round upward after decimal.
    #It always rounds the number up, regardless of the decimal part. 
    print(f"Number of cans needed is: {math.ceil(number_of_cans)}")
    print(f"canes needed: {number_of_cans}")
paint_calculator(wall_height = wall_height, wall_width= wall_width, coverage=coverage)
