# Calculating students average height.

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
total_height = 0
number_of_students = 0
for n in student_heights:
    total_height += n
    number_of_students +=1
# or you can use sum(student_heights) function to add the items of the list.
#average_height = round(total / len(student_heights),2) # using len function.
average_height = round(total_height/number_of_students)
print(f"The average height is: {average_height}")
