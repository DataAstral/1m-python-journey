<p align="center">
  <img src="https://raw.githubusercontent.com/DataAstral/DataAstral/main/banner.png" width="100%">
</p>

# Welcome to DataAstral  
One million projects. One path to mastery.  

Progress: [░░░░░░░░░░] 0.0001% complete  

---

## d10_ternary_operator_try_except_else

**Python Ternary Operator + try / except / else**

This program demonstrates how to combine a **ternary operator** with full error handling using `try / except / else`.

---

## What This Program Does

The program:

• asks the user to enter a number  
• tries to convert the input into an integer  
• if input is invalid → catches the error (`ValueError`)  
• if no error occurs → runs the `else` block  
• uses a **ternary operator** to check even or odd  
• prints a detailed result message  

---

## 💻 Python Code

```python
# Try to get a valid number
try:
    number = int(input("Enter a number: "))

    # Use ternary operator to check even or odd
    result = "Even" if number % 2 == 0 else "Odd"

# Handle invalid input
except ValueError:
    print("Please enter a number")

# Run only if no error occurred
else:
    print(f"You entered {number} your result is {result}")
```

---

## 🔎 Output Preview

### ✅ Valid input
```
Enter a number: 4
You entered 4 your result is Even
```

### ❌ Invalid input
```
Enter a number: hello
Please enter a number
```

---

## Key Concept

- `try` → code that may cause an error  
- `except` → handles the error  
- `else` → runs only if no error happened  
- ternary operator → quick decision in one line  

Example:

```
"Even" if number % 2 == 0 else "Odd"
```

This structure is closer to **real-world programming**, where you separate logic and error handling cleanly.