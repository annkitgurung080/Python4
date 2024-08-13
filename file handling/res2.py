# obj=open("result.txt","r")
name=input("Enter Your Name ::")
phone=input("Enter Your Phone number ::")
print("\n\t EVO STORE \t\n")
print("\n 1.iphone (Rs.210000)\n 2.Samsung(Rs.193000) \n 3.Redmi (rs.50000\n 4.Oneplus(Rs90000) \n 5.Realme(Rs.60000)\n")
iphone_price=0
samsung_price=0
redmi_price=0
oneplus_price=0
realme_price=0
i=0
option=int(input("Enter Your Option(in digit)"))
if option==1:
    qty=int(input("Enter the quantity you want::"))
    iphone_price=210000*qty
    product_name="iphone"
elif option==2:
    qty=int(input("Enter the quantity you want::"))
    samsung_price=193000*qty
    product_name="Samsung"
elif option==3:
    qty=int(input("Enter the quantity you want::"))
    redmi_price=50000*qty
    product_name="redmi"
elif option==4:
    qty=int(input("Enter the quantity you want::"))
    oneplus_price=90000*qty
    product_name="oneplus"
elif option==5:
    qty=int(input("Enter the quantity you want::"))
    realme_price=60000*qty
    product_name="realme"
else:
    print("Invalid Option!!\n\t TRY AGAIN\t\n")
    exit()

print("Delivery option:\n 1.Home Delivery(Rs.1000)\n 2.Pick up(free)")
delivery_option = int(input("Enter the delivery option:"))
delivery_price = 0
if delivery_option == 1:
    delivery_price = 1000

print("Packing:\n 1. Plastice bag(Rs.1000)\n 2.Bag(Rs.2000) \n3.Gift Box(Rs.5000)")
packing_option = int(input("Enter the packing option:"))
packing_price = 0
if packing_option == 1:
    packing_price = 1000
elif packing_option == 2:
    packing_price = 2000
elif packing_option == 3:
    packing_price == 5000

total = iphone_price+realme_price+samsung_price+redmi_price+oneplus_price
tax_amount = 0
print("Location :\n 1.KTM(Rs:13%tax)\n 2.Lalitpur(Rs:0%tax)\n 3.Bhaktapur(Rs:10%tax)")
tax_option = int(input("Enter tax option:"))
if tax_option == 1:
    tax_amount = total*0.13
elif tax_option == 3:
    tax_amount == total*0.1

grand_total = total + delivery_price + packing_price + tax_amount

# FILE HANDLING

obj=open("res.txt","w")
obj.write("\n\t EVO STORE \t\n")
obj.write("================Bill================\n")
obj.write(f"\n Name:{name}")
obj.write(f"\n Phone Number:{phone}")
obj.write(f"\n\tProduct name:{product_name}")
obj.write(f"\n\tQuantity:{qty}")
obj.write(f"\n\tTotal:{total}")
obj.write(f"\n\tDelivery Price:{delivery_price}")
obj.write(f"\n\tPacking Price:{packing_price}")
obj.write(f"\n\tTax amount:{tax_amount}")
obj.write(f"\n\tGrand Total :{grand_total}")
obj.close()