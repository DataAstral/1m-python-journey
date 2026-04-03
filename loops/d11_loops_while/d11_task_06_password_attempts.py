
# task_06_password_attempts.py
attempts = 3
while attempts > 0:
    user_password = input("Enter your password: ")
    if user_password == "admin123":
        print("Welcome")
        break
    else:
        attempts -= 1
        print("Password is incorrect.")
if attempts == 0:
    print("Blocked")
