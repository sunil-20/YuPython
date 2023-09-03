# List notes and codes
fruits = ["Apple", "Pear"]
print(fruits)
print(fruits[0])

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
# Change the values of the list items
states_of_america[1] = "Pencilvania"
print(states_of_america)

# add item at the end of the list.
states_of_america.append("SKLand")
states_of_america.append("SKLand2")
print(states_of_america)

# remove item from the list
## removing the last value
states_of_america.pop(-1)
#removing any item remove the first occurance of the value only. 
#remove method doesn't returns the removed element.
states_of_america.remove("SKLand")
print(states_of_america)

print(states_of_america[-1])
print(states_of_america)