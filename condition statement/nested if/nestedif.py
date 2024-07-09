age=int(input("Enter Your Age ::"))
if age>=18:
    if age>=18 and age<=60:
        print("You are Eligible to vote")
    elif age>60:
        print("You are too Old to Vote")
else:
    print("You are a child")
    