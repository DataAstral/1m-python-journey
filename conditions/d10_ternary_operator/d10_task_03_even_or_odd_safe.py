#Ternary operator in Python 3
try:
    number =int(input("Enter a number: "))
    result = "Even" if number %2 == 0 else "Odd"
    print(result)
except ValueError:
    print("Please enter a number")
