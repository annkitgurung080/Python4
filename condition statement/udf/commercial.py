def get_product_info(option):
    products = {
        1: {"name": "iPhone", "price": 210000},
        2: {"name": "Samsung", "price": 193000},
        3: {"name": "Redmi", "price": 50000},
        4: {"name": "OnePlus", "price": 90000},
        5: {"name": "Realme", "price": 60000}
    }
    return products.get(option, {"name": "Invalid Option", "price": 0})

def calculate_total(product, qty):
    return product["price"] * qty

def get_delivery_option():
    print("Delivery option:\n 1. Home Delivery (Rs.1000)\n 2. Pick up (free)")
    delivery_option = int(input("Enter the delivery option: "))
    if delivery_option == 1:
        return 1000
    else:
        return 0

def get_packing_option():
    print("Packing:\n 1. Plastic bag (Rs.1000)\n 2. Bag (Rs.2000) \n3. Gift Box (Rs.5000)")
    packing_option = int(input("Enter the packing option: "))
    if packing_option == 1:
        return 1000
    elif packing_option == 2:
        return 2000
    elif packing_option == 3:
        return 5000
    else:
        return 0

def calculate_tax(total, tax_option):
    if tax_option == 1:
        return total * 0.13
    elif tax_option == 3:
        return total * 0.1
    else:
        return 0

def print_bill(product, qty, total, delivery_price, packing_price, tax_amount, grand_total):
    print("================Bill================")
    print("Product name:", product["name"])
    print("Quantity:", qty)
    print("Total:", total)
    print("Delivery Price:", delivery_price)
    print("Packing Price:", packing_price)
    print("Tax amount:", tax_amount)
    print("Grand Total :", grand_total)

def main():
    print("\n\t EVO STORE \t\n")
    print("\n 1. iPhone (Rs.210000)\n 2. Samsung (Rs.193000)\n 3. Redmi (Rs.50000)\n 4. OnePlus (Rs.90000)\n 5. Realme (Rs.60000)\n")
    option = int(input("Enter Your Option (in digit): "))
    product = get_product_info(option)
    if product["name"] == "Invalid Option":
        print("Invalid Option!!\n\t TRY AGAIN\t\n")
        exit()
    qty = int(input("Enter the quantity you want: "))
    total = calculate_total(product, qty)
    delivery_price = get_delivery_option()
    packing_price = get_packing_option()
    tax_option = int(input("Enter tax option (1 for KTM, 2 for Lalitpur, 3 for Bhaktapur): "))
    tax_amount = calculate_tax(total, tax_option)
    grand_total = total + delivery_price + packing_price + tax_amount
    print_bill(product, qty, total, delivery_price, packing_price, tax_amount, grand_total)

if __name__ == "__main__":
    main()
    
    # Functionwith default argument
    # function generator 
    # function scope 
    # nested function
    # lambda function
    # recursive function
    # map function 
    # filter function
    # reduce function 
    # decorator function
    # module