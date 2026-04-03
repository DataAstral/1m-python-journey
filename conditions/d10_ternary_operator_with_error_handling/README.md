<p align="center">
  <img src="https://raw.githubusercontent.com/DataAstral/DataAstral/main/banner.png" width="100%">
</p>

# Welcome to DataAstral  
One million projects. One path to mastery.  

Progress: [░░░░░░░░░░] 0.0001% complete  

---

## d10_ternary_operator_with_error_handling

**Python Ternary Operator + Error Handling (try / except)**

This program demonstrates how to safely use a **ternary operator** together with **error handling**.

---

##  What This Program Does

The program:

• asks the user to enter a number  
• tries to convert the input into an integer  
• if conversion fails → catches the error (`ValueError`)  
• if input is valid → checks if the number is even or odd  
• uses a **ternary operator** to decide the result  
• prints the result or an error message  

---

## 💻 Python Code

```python
# Try to get a valid number from the user
try:
    number = int(input("Enter a number: "))

    # Use ternary operator to check even or odd
    result = "Even" if number % 2 == 0 else "Odd"

    # Print result
    print(result)

# Handle invalid input
except ValueError:
    print("Please enter a number")
```

---

## 🔎 Output Preview

### ✅ Valid input
```
Enter a number: 10
Even
```

### ❌ Invalid input
```
Enter a number: hello
Please enter a number
```

---

## Key Concept

- `try` → code that may cause an error  
- `except` → handles the error (`ValueError`)  
- ternary operator → short decision in one line  

Example:

```
"Even" if number % 2 == 0 else "Odd"
```

This combination makes your program **safe and clean** — it won’t crash if the user enters invalid data.