# Band Name Generator
# print a welcome message
print("Welcome to the band name generator!")

# Ask user for city grew up and save in a variable.
city_born = input("In which city you were born?\n")

# Ask user for their pet's name and save in a variable.
pet_name = input("What is your favourite pet name?\n")

# Create a new variable name called band name by concat all info above.
band_name = city_born + " " + pet_name

# Print the band_name variable with initial info.
print("Your band name is: " + band_name)