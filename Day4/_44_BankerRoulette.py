# Who is gona pay today's bill?
import random
names = input("Give the list of the names who are together dining and separate the name with comma.")
names_list = names.split(',')
list_length = len(names_list)-1
random_index = random.randint(0, list_length)
random_person = names_list[random_index]
print(f"{random_person} is going to buy the meal today!")

random_person = random.choice(names_list)
print(f"{random_person} is going to buy the meal today2!")