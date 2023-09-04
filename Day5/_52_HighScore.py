#Solution one
student_scores = input("Input a list of students score: ").split()
# convert string to numeric
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
heighest_score = 0
for score in student_scores:
    if score > heighest_score:
        heighest_score = score
print(heighest_score)

# Solution two
student_scores = input("Input a list of students score: ").split()
# convert string to numeric
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
# create a variable to compare each values in the list
compare = 0
# add each item to the variable/ this is not necessary
# for score in student_scores:
#     compare = score
# compare to the created variable if the value is larger or not.
for score in student_scores:
    if score > compare:
        compare = score
# print the value
print(f"The heighest score in the clas is: {compare}")