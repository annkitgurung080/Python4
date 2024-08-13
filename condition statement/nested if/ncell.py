# 100 min minimum
#1-10
#ntc-ntc->2.5
# ntc-ncell ->3.5
#ncell=ncell->5
# ncell to ->4
print("\n 1.NTC \n2.Ncall \n")
owner_sim=int(input("Select Your Sim :"))
print("\n 1.NTC \n2.Ncell \n")
customer_sim=int(input("Enter in which sim you Want to call:: "))
cus_num=int(input("Dail the Number:: "))
call_duration=int(input("Enter Call Duration:: "))
if call_duration>100:
    print("Dear Costumer. \n\tYou don't have bonus beacause your Call Duration exceed 100 Minutes.\t\n")
    exit()
else:
    if owner_sim==1 and customer_sim==1:
        bonus=2.5
        if call_duration>=1 and call_duration<=10:
            print(f"Your total Balance is {bonus}")
        elif call_duration>10 and call_duration<=20:
            total_bonus=bonus*2
            print(f"Your Total Bonus is ::{total_bonus}")
        elif call_duration>20 and call_duration<=30:
            total_bonus=bonus*3
            print(f"Your Total Bonus is ::{total_bonus}")
        elif call_duration>30 and call_duration<=40:
            total_bonus=bonus*4
            print(f"Your Total Bonus is ::{total_bonus}")
        elif call_duration>40 and call_duration<=50:
            total_bonus=bonus*5
            print(f"Your Total Bonus is ::{total_bonus}")
        elif call_duration>50 and call_duration<=60:
            total_bonus=bonus*6
            print(f"Your Total Bonus is ::{total_bonus}")
        elif call_duration>60 and call_duration<=70:
            total_bonus=bonus*7
            print(f"Your Total Bonus is ::{total_bonus}")
        elif call_duration>70 and call_duration<=80:
            total_bonus=bonus*8
            print(f"Your Total Bonus is ::{total_bonus}")
        elif call_duration>80 and call_duration<=90:
            total_bonus=bonus*9
            print(f"Your Total Bonus is ::{total_bonus}")
        elif call_duration>90 and call_duration<=100:
            total_bonus=bonus*10
            print(f"Your Total Bonus is ::{total_bonus}")
    elif owner_sim==1 and customer_sim==2:
        bonus=3.5
        if call_duration>=1 and call_duration<=10:
            print(f"Your total Balance is {bonus}")
        elif call_duration>10 and call_duration<=20:
            total_bonus=bonus*2
            print(f"Your Total Bonus is ::{total_bonus}")
        elif call_duration>20 and call_duration<=30:
            total_bonus=bonus*3
            print(f"Your Total Bonus is ::{total_bonus}")
        elif call_duration>30 and call_duration<=40:
            total_bonus=bonus*4
            print(f"Your Total Bonus is ::{total_bonus}")
        elif call_duration>40 and call_duration<=50:
            total_bonus=bonus*5
            print(f"Your Total Bonus is ::{total_bonus}")
        elif call_duration>50 and call_duration<=60:
            total_bonus=bonus*6
            print(f"Your Total Bonus is ::{total_bonus}")
        elif call_duration>60 and call_duration<=70:
            total_bonus=bonus*7
            print(f"Your Total Bonus is ::{total_bonus}")
        elif call_duration>70 and call_duration<=80:
            total_bonus=bonus*8
            print(f"Your Total Bonus is ::{total_bonus}")
        elif call_duration>80 and call_duration<=90:
            total_bonus=bonus*9
            print(f"Your Total Bonus is ::{total_bonus}")
        elif call_duration>90 and call_duration<=100:
            total_bonus=bonus*10
            print(f"Your Total Bonus is ::{total_bonus}")
    elif owner_sim==2 and customer_sim==2:
        bonus=5
        if call_duration>=1 and call_duration<=10:
            print(f"Your total Balance is {bonus}")
        elif call_duration>10 and call_duration<=20:
            total_bonus=bonus*2
            print(f"Your Total Bonus is ::{total_bonus}")
        elif call_duration>20 and call_duration<=30:
            total_bonus=bonus*3
            print(f"Your Total Bonus is ::{total_bonus}")
        elif call_duration>30 and call_duration<=40:
            total_bonus=bonus*4
            print(f"Your Total Bonus is ::{total_bonus}")
        elif call_duration>40 and call_duration<=50:
            total_bonus=bonus*5
            print(f"Your Total Bonus is ::{total_bonus}")
        elif call_duration>50 and call_duration<=60:
            total_bonus=bonus*6
            print(f"Your Total Bonus is ::{total_bonus}")
        elif call_duration>60 and call_duration<=70:
            total_bonus=bonus*7
            print(f"Your Total Bonus is ::{total_bonus}")
        elif call_duration>70 and call_duration<=80:
            total_bonus=bonus*8
            print(f"Your Total Bonus is ::{total_bonus}")
        elif call_duration>80 and call_duration<=90:
            total_bonus=bonus*9
            print(f"Your Total Bonus is ::{total_bonus}")
        elif call_duration>90 and call_duration<=100:
            total_bonus=bonus*10
            print(f"Your Total Bonus is ::{total_bonus}")
    elif owner_sim==2 and customer_sim==1:
        bonus=4
        if call_duration>=1 and call_duration<=10:
            print(f"Your total Balance is {bonus}")
        elif call_duration>10 and call_duration<=20:
            total_bonus=bonus*2
            print(f"Your Total Bonus is ::{total_bonus}")
        elif call_duration>20 and call_duration<=30:
            total_bonus=bonus*3
            print(f"Your Total Bonus is ::{total_bonus}")
        elif call_duration>30 and call_duration<=40:
            total_bonus=bonus*4
            print(f"Your Total Bonus is ::{total_bonus}")
        elif call_duration>40 and call_duration<=50:
            total_bonus=bonus*5
            print(f"Your Total Bonus is ::{total_bonus}")
        elif call_duration>50 and call_duration<=60:
            total_bonus=bonus*6
            print(f"Your Total Bonus is ::{total_bonus}")
        elif call_duration>60 and call_duration<=70:
            total_bonus=bonus*7
            print(f"Your Total Bonus is ::{total_bonus}")
        elif call_duration>70 and call_duration<=80:
            total_bonus=bonus*8
            print(f"Your Total Bonus is ::{total_bonus}")
        elif call_duration>80 and call_duration<=90:
            total_bonus=bonus*9
            print(f"Your Total Bonus is ::{total_bonus}")
        elif call_duration>90 and call_duration<=100:
            total_bonus=bonus*10
            print(f"Your Total Bonus is ::{total_bonus}")
    else:
        print("\nDear Costumer. \n\tYou Have Less than 1 Minutes So You Don't Have Bonus\t\n")
     