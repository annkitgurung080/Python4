def take_value():
    p=int(input("Enter the p :"))
    t=int(input("Enter the t :"))
    r=int(input("Enter the r :"))
    return [p,t,r]

def calculate():
    p,t,r= take_value()
    return p*t*r/100
def display():
    print("Simple Intrest:",calculate())
    
display()