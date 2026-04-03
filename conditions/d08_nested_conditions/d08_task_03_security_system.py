# Security access system with user input

# Ask the user for their age
age = int(input("Enter your age: "))

# Ask if the user has an ID
has_id_input = input("Do you have an ID? (yes/no): ")

# Ask if the user knows the security code
knows_code_input = input("Do you know the security code? (yes/no): ")

# Convert answers to boolean values
has_id = has_id_input.lower() == "yes"
knows_code = knows_code_input.lower() == "yes"

# First check: is the user an adult?
if age >= 18:
    # Second check: does the user have an ID?
    if has_id:
        # Third check: does the user know the security code?
        if knows_code:
            print("Full access granted")
        else:
            print("Partial access: ID confirmed, but security code is missing")
    else:
        # User is adult, but has no ID
        print("Access denied: ID card required")
else:
    # User is under 18
    print("Access denied: adults only")
