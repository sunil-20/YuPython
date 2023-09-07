
food = {
    "Vegetables":["Pumpkin","Cauliflower","Beans","Eggplant","Chayote"],
     "Fruits": ["Apple","Pear","Bananas","Blueberry"],
}
#fetching items from the dictionary
fruits = food["Fruits"]
vegetables = food["Vegetables"]

# add new entry
food["Beverages"]= ["Soda", "Water", "Smoothie","Coffee","Tea","Lemonade","Juice"]
print(fruits)
print(vegetables)
print(f'Beverages: {food["Beverages"]}')

#creating empty dictionary and adding items in it
kitchen_utensils = {}
kitchen_utensils["small_utensils"]= ["Fork","Spoon","Knife","lemon squeezer"]
print(kitchen_utensils)
print(kitchen_utensils["small_utensils"])
kitchen_utensils["Large_utensils"]= "Slow Cooker"
print(kitchen_utensils)