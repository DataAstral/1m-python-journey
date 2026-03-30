# Access control system

# Store user data
age = 20
has_ticket = True

# Check access conditions
if age >= 18 and has_ticket:
    print("Welcome!")
elif age >= 18 and not has_ticket:
    print("You need a ticket.")
else:
    print("Access denied: you are under 18.")
