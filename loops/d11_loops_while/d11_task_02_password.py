# task_02_password.py
password = ""
while password != "123456789":
    password = input("Enter your password: ")
    if password == "123456789":
        print("Password is correct")
    else:
        print("Password is incorrect")
