#WAP to enter NY NUMBER DIVISIBLE BY 3 AND 5
# is , is not ,not ,in
num = int(input("Enter any number ::"))
if num % 3==0 and num%5==0:
    print(f"{num} is divisible by 5 and 3")
else:
    if num % 3 == 0 :
        print(f"{num}is divisible by 3 only not by 5")
    elif num%5 == 0:
        print(f"{num} is divisible by 5 only not by 3")
    else:
        print(f"{num}is not divisible by both 5 and 3")