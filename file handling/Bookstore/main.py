# .strip removes leading and trailing space
# .lower() converts to lower case
# .upper() converts to upper case
# .replace() replaces a character with another character
# .find() finds the index of a character in a string
import os

if not os.path.exists("userss.txt"):
    handle= open("userss.txt","w")
    handle.close()
    
def register():
  print("==========Register User==============")
  username = input("Enter your username: ").strip()
  if username in open("userss.txt","r").read(): 
    print("Username Already Exists.")
    exit()
  password = input("Enter your password: ")
  confirm_password= input("Confirm Password: ").strip()
  if password!=confirm_password:
        print("Passwords do not match.")
        exit()
  with open("userss.txt", "a") as file:
      file.write(f"username:{username},password:{password}\n")
      print("User Registered Sucessfully")
      
# register()

def login():
    print("===============login Users===============") 
    username=input("Enter Username : ")
    password=input("Enter Password : ")
    with open("userss.txt","r") as file:
        users = file.readlines()
        is_login = False
        for user in users:
            user = user.strip().split(",")
            uname = user[0].split(":")[1]
            upass = user[1].split(":")[1]
            if username == uname and password == upass:
                is_login = True
            if is_login:
                    print("Login Sucessfully")
            else:
                print("Invalid Username or Password")
                exit()
login()
        
                     