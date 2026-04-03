try:
    number = int(input("Enter a number: "))
    print(f" Your number: {number}")
except ValueError:
    print("That's not a number")
finally:
    print("Goodbye")