student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
updated_dictionary = {}

for i in student_scores:
    if student_scores[i]>90:
        updated_dictionary[i]= "Outstanding"
    elif student_scores[i]>80:
        updated_dictionary[i]= "Exceeds Expectations"
    elif student_scores[i]>70:
        updated_dictionary[i]= "Acceptable"
    else:
        updated_dictionary[i]= "Fail"

print(updated_dictionary)
