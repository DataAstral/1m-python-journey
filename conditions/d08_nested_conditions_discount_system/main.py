# Discount system with nested conditions

age = 20
is_member = True

# Check if the user is an adult
if age >= 18:
    # Check membership status
    if is_member:
        print("20% discount for members")
    else:
        print("No discount, but you are an adult")
else:
    print("Adults only")
