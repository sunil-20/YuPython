print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_name1 = name1.lower()
lower_name2 = name2.lower()
name_together = lower_name1+lower_name2

# Counting TRUE
t = name_together.count('t')
r = name_together.count('r')
u = name_together.count('u')
e = name_together.count('e')


# Counting LOVE
l = name_together.count('l')
o = name_together.count('o')
v = name_together.count('v') 
e = name_together.count('e')

true_score = t+r+u+e
love_score = l+o+v+e

final_score = int(str(true_score)+str(love_score))

if final_score <10 or final_score >90:
    print(f"Your score is {final_score}, you go together like coke and mentos.")
elif final_score >40 and final_score<50:
    print(f"Your score is {final_score}, you are alright together.")
else:
    print(f"Your score is {final_score}.")