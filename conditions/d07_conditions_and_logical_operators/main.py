# Access control system

# Ask the user for their age
age = int(input("Enter your age: "))

# Ask if the user knows the password
password = input("Do you know the password? (yes/no): ")

# Ask if the user has a token
token = input("Do you have a token? (yes/no): ")

# Check conditions
has_password = password == "yes"
has_token = token == "yes"

# Access logic
if age >= 18 and (has_password or has_token):
    print("✅ Access granted")
else:
    print("❌ Access denied")
