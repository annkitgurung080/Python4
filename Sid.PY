name=input("Enter Name :")
sub1=float(input("Enter marks in subject 1 ::"))
sub2=float(input("Enter marks in subject 2 ::"))
sub3=float(input("Enter marks in subject 3 ::"))
sub4=float(input("Enter marks in subject 4 ::"))
sub5=float(input("Enter marks in subject 5 ::"))
Total=sub1+sub2+sub3+sub4+sub5
print(f"Name:{name}")
print(f"Total marks in all subject :{Total}/500")
Percentage=(Total/500)*100
print(f"Your Percentage is :{Percentage}")