num_of_students = int(input("How many students do you want to enter? "))

name_list = []
grade_list = []
letter_grade_list = []
status_list = []

for student in range(num_of_students):
    name = input("What is the student's name? ")
    grade = int(input("What is the student's grade? (0-100) "))

    name_list.append(name)
    grade_list.append(grade)

average_grade = sum(grade_list)/num_of_students

for x in range(len(grade_list)):
    student_grade = grade_list[x]
    status = "Passed"

    if student_grade >= 90 and student_grade <= 100:
        letter_grade = "A"
    
    elif student_grade >= 80 and student_grade <= 89:
        letter_grade = "B"
    
    elif student_grade >= 70 and student_grade <= 79:
        letter_grade = "C"
    
    elif student_grade >= 60 and student_grade <= 69:
        letter_grade = "D"
    
    elif student_grade < 60:
        letter_grade = "F"
        status = "Failed"

    letter_grade_list.append(letter_grade)
    status_list.append(status)


print(f"{'Student Name':<15}{'Grade':<10}{'Letter Grade':<15}{'Status':<10}")

for y in range(num_of_students):
    print(f"{name_list[y]:<15}{grade_list[y]:<10}{letter_grade_list[y]:<15}{status_list[y]:<10}")

print(f"The average grade is {average_grade:.2f}.")
