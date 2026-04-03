try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That's not a number")
else:
    print(f"Thank you! Your number is: {number}")