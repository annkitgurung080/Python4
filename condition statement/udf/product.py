import os

if not os.path.exists("bill.txt"):
    handle = open("bill.txt", "w")
    handle.close()

def bill():
    print("----------------------Bill-------------------------")
    name = input("Enter Product Name:").strip()
    
    with open("bill.txt", "r") as file:
        if name in file.read():
            print("Name already exists")
            return  
    
        price = float(input("Enter Price:").strip())  
        quantity = int(input("Enter quantity of product:").strip())
       
    
    total = price * quantity
    
    with open("bill.txt", "a") as file:
        file.write(f"Name: {name}, Price: {price}, Quantity: {quantity}, Total: {total}\n")
        print("Billing Successful")

def buy():
    print("===================BUY=======================")
    name = input("Enter product name: ").strip()
    price = float(input("Enter Price:").strip())  
    quantity = int(input("Enter quantity of product:").strip())
    

    with open("bill.txt", "r") as file:
        found = False
        for line in file:
            product = line.strip().split(",")
            product_name = product[0].split(":")[1].strip()
            product_quantity = int(product[2].split(":")[1].strip())

            if name == product_name:
                found = True
                if quantity <= product_quantity:
                    total = price * quantity
                    print(f"Total: {total}")
                else:
                    print("Insufficient quantity available.")
                break
        
        if not found:
            print("Product not found.")

buy()