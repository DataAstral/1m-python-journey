<p align="center">
  <img src="https://raw.githubusercontent.com/DataAstral/DataAstral/main/banner.png" width="100%">
</p>

# Welcome to DataAstral  
One million projects. One path to mastery.  

Progress: [░░░░░░░░░░] 0.0001% complete  

---

## d09_try_except_input_validation

**Python Error Handling — `try`, `except`, and safe user input**

This program demonstrates how to safely handle user input, validate data, and prevent crashes using exception handling.

---

### What This Program Does

The program:

1. Asks the user to enter a number  
2. Checks if the input is empty  
3. Tries to convert the input into an integer  
4. Handles invalid input using `except (ValueError, TypeError)`  
5. Displays whether the number is positive, negative, or zero  
6. Performs a simple calculation with the number  
7. Finishes the program safely without crashing  

---

## 💻 Python Code

```python
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
```

---

## 🔎 Output Preview

### ✅ Valid input
```text
=== NUMBER VALIDATION PROGRAM ===
Enter a number: 8
You entered: 8
This is a positive number.
Your number + 10 = 18
Program finished.
```

### ❌ Invalid input
```text
=== NUMBER VALIDATION PROGRAM ===
Enter a number: hello
Invalid data type. Please enter a valid number.
Program finished.
```

### ❌ Empty input
```text
=== NUMBER VALIDATION PROGRAM ===
Enter a number: 
Invalid data type. Please enter a valid number.
Program finished.
```

---

### Key Concept

- `try` → code that may cause an error  
- `except` → handles the error  
- `ValueError` → happens when conversion to integer fails  
- `TypeError` → manually raised for empty input  

This structure helps you write safer programs that handle user mistakes without crashing.