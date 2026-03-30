# Ask the user to enter their age (as a string)
age_input = input("Enter your age: ")

# Convert the input into an integer
age = int(age_input)

# Check the condition: if age is 18 or older — access is allowed
if age >= 18:
    print("Welcome to the website!")
# Otherwise, calculate how many years are left until 18
else:
    years_left = 18 - age
    print("Too early. Come back in", years_left, "years.")
