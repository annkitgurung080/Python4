print("*******BASIC CALCULATOR*******")
n1=int(input("Enter First Number ::"))
n2=int(input("Enter Second Number ::"))
ch=input("Enter your Choice (+,-,/,*)::")
match ch:
    case '+':
        output=n1+n2
        print(f"The Sum of {n1}and {n2} is {output}")
    case '-':
        output=n1-n2
        print(f"The Output is :{output}")
    case '*':
        output=n1*n2
        print(f"The Output is {output}")
    case '/':
        output=n1/n2
        print(f"The output is {output}")
    case _:#this is used in default 
        print("\tInvalid Choice !!\t")