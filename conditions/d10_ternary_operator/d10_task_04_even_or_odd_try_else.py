#Ternary operator in Python 4
try:
    number =int(input("Enter a number: "))
    result = "Even" if number %2 == 0 else "Odd"
except ValueError:
    print("Please enter a number")
else:
    print(f"You entered {number} your result is {result}")