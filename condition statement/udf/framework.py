from tkinter import *
import random

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x700+0+0")
        self.root.maxsize(width=1280, height=700)
        self.root.minsize(width=1280, height=700)
        self.root.title("Billing Software")

        # Variables
        self.cus_name = StringVar()
        self.c_phone = StringVar()
        x = random.randint(1000, 9999)
        self.c_bill_no = StringVar()
        self.c_bill_no.set(str(x))

        self.bath_soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.hair_spray = IntVar()
        self.body_lotion = IntVar()
        self.rice = IntVar()
        self.daal = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.maza = IntVar()
        self.coke = IntVar()
        self.frooti = IntVar()
        self.nimko = IntVar()
        self.biscuits = IntVar()
        self.total_cosmetics = StringVar()
        self.total_grocery = StringVar()
        self.total_other = StringVar()
        self.tax_cos = StringVar()
        self.tax_groc = StringVar()
        self.tax_other = StringVar()

        # Title of App
        title = Label(self.root, text="Billing Software", bd=12, relief=GROOVE, fg="white", bg="#074463",
                      font=("times new roman", 30, "bold"), pady=3).pack(fill=X)

        # Customers Frame
        F1 = LabelFrame(text="Customer Details", font=("time new roman", 12, "bold"), fg="gold", bg="#074463",
                         relief=GROOVE, bd=10)
        F1.place(x=0, y=80, relwidth=1)

        # Customer Name
        cname_lbl = Label(F1, text="Customer Name", bg="#074463", fg="white",
                           font=("times new roman", 15, "bold")).grid(row=0, column=0, padx=10, pady=5)
        cname_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.cus_name)
        cname_en.grid(row=0, column=1, ipady=4, ipadx=30, pady=5)

        # Customer Phone
        cphon_lbl = Label(F1, text="Phone No", bg="#074463", fg="white", font=("times new roman", 15, "bold")).grid(
            row=0, column=2, padx=20)
        cphon_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.c_phone)
        cphon_en.grid(row=0, column=3, ipady=4, ipadx=30, pady=5)

        # Customer Bill No
        cbill_lbl = Label(F1, text="Bill No.", bg="#074463", fg="white", font=("times new roman", 15, "bold")).grid(
            row=0, column=4, padx=20)
        cbill_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.c_bill_no)
        cbill_en.grid(row=0, column=5, ipady=4, ipadx=30, pady=5)

        # ... rest of the code ...

root = Tk()
obj = Bill_App(root)
root.mainloop()