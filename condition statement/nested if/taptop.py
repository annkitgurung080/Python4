print("=============Computer Bazar============")
print("\n1.Dell(Rs.20000)\n 2.Toshiba(Rs.30000)\n 3.Mac(Rs.500000)")
dell_price = 0
toshiba_price = 0
mac_price = 0
product_name = 0
quantity = 0

option = int(input("Enter the option ::"))

if option == 1:
    quantity = int(input("Enter the quantity: "))
    dell_price = 20000*quantity
    product_name = "Dell"
elif option == 2:
    quantity = int(input("Enter the quantity: "))
    toshiba_price = 30000*quantity
    product_name = "Toshiba"
elif option == 3:
    quantity = int(input("Enter the quantity: "))
    toshiba_price = 50000*quantity
    product_name = "Mac"
else:
    print("Invalid option")
    exit()

print("Delivery option:\n 1.Home Delivery(Rs.1000)\n 2.Pick up(free)")
delivery_option = int(input("Enter the delivery option:"))
delivery_price = 0
if delivery_option == 1:
    delivery_price = 1000

print("Packing:\n 1. Plastice bag(Rs.1000)\n 2.Bag(Rs.2000) \n3.Gift Box(Rs.5000)")
packing_option = 0
packing_price = 0
if packing_option == 1:
    packing_price = 1000
elif packing_option == 2:
    packing_price = 2000
elif packing_option == 3:
    packing_price == 5000

total = dell_price+toshiba_price+mac_price
tax_amount = 0
print("Location : 1.KTM(Rs:13%tax)\n 2.Lalitpur(Rs:0%tax)\n 3.Bhaktapur(Rs:10%tax)")
tax_option = int(input("Enter tax option:"))
if tax_option == 1:
    tax_amount = total*0.13
elif tax_option == 3:
    tax_amount == total*0.1

grand_total = total + delivery_price + packing_price + tax_amount

print("================Bill================")
print("Product name:",product_name)
print("Quantity:",quantity)
print("Total:",total)
print("Delivery Price:",delivery_price)
print("Packing Price:",packing_price)
print("Tax amount:",tax_amount)
print("Grand Total :", grand_total)