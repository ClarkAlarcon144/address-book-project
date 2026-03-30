def calculate_grade(scores):
    average = sum(scores)/len(scores)

    if average >= 90 and average <= 100:
        grade = "A"
        
    elif average >= 80 and average <= 89:
        grade = "B"

    elif average >= 70 and average <= 79:
        grade = "C"

    elif average >= 60 and average <= 69:
        grade = "D"

    elif average < 60:
        grade = "F"

    return {
        "average": average,
        "grade": grade
    }