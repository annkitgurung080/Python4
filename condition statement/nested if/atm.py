print("******************ATM MACHINE*******************")
pin=1234
ttlamt=10000
n = int(input("Enter Your Pin ::"))
if n==pin:
    print("CARD ACCESSED")
    print("1.Withdraw")
    print("2.Balance Inquiry")
    ch=int(input("Enter your Choice ::"))
    if ch==1:
        withdraw = int(input("Enter Amt to withdraw ::"))
        if ttlamt>=withdraw:
            print("Your Amt is Withdrawn")
        else:
            print("Unsufficient Balance")
    elif ch==2:
        print(f"Your Total Balance is {ttlamt}")
    else:
        print("Invalid Input")
else:
    print("Invalid Pin \n TRY AGAIN ")
    