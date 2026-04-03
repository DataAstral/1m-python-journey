try:
    number_input = int(input("Please enter a number: "))
    print(10 / number_input)
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
