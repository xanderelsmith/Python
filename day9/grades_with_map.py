student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades = student_scores
# This is the scoring criteria: 

# - Scores 91 - 100: Grade = "Outstanding" 

# - Scores 81 - 90: Grade = "Exceeds Expectations" 

# - Scores 71 - 80: Grade = "Acceptable" 

# - Scores 70 or lower: Grade = "Fail" 
for data in student_grades:
    print(data,student_grades[data])
    if student_grades[data] > 90:
        student_grades[data] = "Outstanding"
    elif student_grades[data]>80:
        student_grades[data]="Exceeds Expectations" 
    elif (student_grades[data] > 70):
        student_grades[data] = "Acceptable"
    else:
        student_grades[data]="Fail"
print(student_grades)
        
