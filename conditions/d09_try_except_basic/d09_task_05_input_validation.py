# Safe number input with error handling

print("=== NUMBER VALIDATION PROGRAM ===")

try:
    # Ask user for input
    user_input = input("Enter a number: ")

    # Check if input is empty
    if user_input == "":
        raise TypeError

    # Convert to integer
    number = int(user_input)

    # Show result
    print(f"You entered: {number}")

    # Extra logic
    if number > 0:
        print("This is a positive number.")
    elif number < 0:
        print("This is a negative number.")
    else:
        print("This number is zero.")

    # Extra calculation
    print(f"Your number + 10 = {number + 10}")

# Handle errors
except (ValueError, TypeError):
    print("Invalid data type. Please enter a valid number.")

print("Program finished.")