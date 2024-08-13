def calculate_marksheet(marks):
    total_marks = sum(marks.values())
    percentage = (total_marks / sum(max_marks.values())) * 100
    grade = get_grade(percentage)

    marksheet = {
        'total_marks': total_marks,
        'percentage': percentage,
        'grade': grade
    }
    return marksheet

def get_grade(percentage):
   
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'


max_marks = {'Math': 100, 'Science': 100, 'English': 100}
marks = {'Math': 80, 'Science': 70, 'English': 90}
marksheet = calculate_marksheet(marks)
print(marksheet)