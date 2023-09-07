
# food = {
#     "Vegetables":["Pumpkin","Cauliflower","Beans","Eggplant","Chayote"],
#      "Fruits": ["Apple","Pear","Bananas","Blueberry"],
# }
# #fetching items from the dictionary
# fruits = food["Fruits"]
# vegetables = food["Vegetables"]

# # add new entry
# food["Beverages"]= ["Soda", "Water", "Smoothie","Coffee","Tea","Lemonade","Juice"]
# print(fruits)
# print(vegetables)
# print(f'Beverages: {food["Beverages"]}')

#creating empty dictionary and adding items in it
kitchen_utensils = {}
kitchen_utensils["Small_utensils"]= ["Fork","Spoon","Knife","lemon squeezer"]
#print(kitchen_utensils)
#print(kitchen_utensils["Small_utensils"])
kitchen_utensils["Large_utensils"]= "Slow Cooker"
#print(kitchen_utensils)

# to empty the created dictionary
# kitchen_utensils = {}
# print(f"Empty dict: {kitchen_utensils}")

#looping 
for value in kitchen_utensils.values():
    print(value)
    #print(kitchen_utensils[key])
