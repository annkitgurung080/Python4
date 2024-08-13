num_student=int(input("Enter the number of student ::"))
student_marks = []

x=1

while x<=num_student:
    print(f"=============Student Id {x}==================")
    for i in range (1):
        nep=int(input("Enter the marks of Nepali: "))
        eng=int(input("Enter the marks of English: "))
        math=int(input("Enter the marks of Math: "))
        sci=int(input("Enter the marks in Science: "))
        pop=int(input("Enter the marks of Population: "))
        total=nep+eng+math+sci+pop
        student_marks.append(total)
    x+=1
    
    
    
for total in student_marks:
    per=total/5
    grade=""
    if per>=80:
        grade="A"
    elif per>=60:
        grade="B"
    elif per>=40:
        grade="C"
    else:
        grade="D"
        
    print(f"Total Marks :{total} Percentage:{per} Grade: {grade}")