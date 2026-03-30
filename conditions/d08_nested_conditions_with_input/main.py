# Authentication system with user input

# Ask user to enter username
username = input("Enter username: ").lower()

# Ask user to enter password
password = input("Enter password: ").lower()

# Check username first
if username == "admin":
    # Then check password
    if password == "1234":
        print("Welcome!")
    else:
        print("Incorrect password")
else:
    print("User not found")
