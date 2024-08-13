name=input("Enter Name :")
sub1=float(input("Enter marks in subject 1 ::"))
sub2=float(input("Enter marks in subject 2 ::"))
sub3=float(input("Enter marks in subject 3 ::"))
sub4=float(input("Enter marks in subject 4 ::"))
sub5=float(input("Enter marks in subject 5 ::"))
Total=sub1+sub2+sub3+sub4+sub5
Percentage=(Total/500)*100   
obj=open("result.txt","w")
obj.write("\t\t\t\t\t Marks Sheet \t\t\t\t\t\n")
obj.write(f"Name :{name}\n")

obj.write(f"1.Subject 1 :\t{sub1}\n")
obj.write(f"2.Subject 2 :\t{sub2}\n")
obj.write(f"3.Subject 3 :\t{sub3}\n")
obj.write(f"4.Subject 4 :\t{sub4}\n")
obj.write(f"5.Subject 5 :\t{sub5}\n")
obj.write(f"      Total :\t{Total}\n")
obj.write(f"\t\t\t\t\t\t Your Percentage :{Percentage}\n")
if Percentage>=35 and Percentage<=45:
    obj.write(" \t\t\t\t\t\t GRADE:: D\n")
elif Percentage>=45 and Percentage<=60:
        obj.write(" \t\t\t\t\t\t GRADE:: C\n")
elif Percentage>=60 and Percentage<=75:
        obj.write(" \t\t\t\t\t\t GRADE:: B\n")
elif Percentage>=75 and Percentage<=100:
        obj.write(" \t\t\t\t\t\t GRADE:: A\n")
else:
        obj.write(" \t\t\t\t\t\t GRADE:: Fail\n")    
obj.close()