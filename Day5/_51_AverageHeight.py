# Calculating students average height.

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
total = 0
length = 0
for n in student_heights:
    total += n
    length+=1
# or you can use sum(student_heights) function to add the items of the list.
#average_height = round(total / len(student_heights),2) # using len function.
average_height = round(total/length)
print(f"The average height is: {average_height}")
