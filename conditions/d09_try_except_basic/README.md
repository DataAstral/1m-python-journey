<p align="center">
  <img src="https://raw.githubusercontent.com/DataAstral/DataAstral/main/banner.png" width="100%">
</p>

# Welcome to DataAstral

One million projects. One path to mastery.

Progress: [░░░░░░░░░░] 0.0001% complete

---

## d09_try_except_basic

**Python Error Handling (`try`, `except`, `else`, `finally`)**

This folder contains small Python programs that demonstrate how basic error handling works in Python.

These programs show how to catch invalid input, handle different exceptions, and keep programs running safely.

---

## What These Programs Do

These programs demonstrate:

• how to use `try` and `except`  
• how to catch `ValueError` and `ZeroDivisionError`  
• how to use `else` after successful code  
• how to use `finally` for code that always runs  
• how to validate input before using it  

The examples gradually become slightly more complex.

---

## 💻 Program 1 — Division with Input

This program asks for a number and handles invalid input.

```python
try:
    number_input = int(input("Please enter a number: "))
    print(10 / number_input)
except:
    print("Please enter a number")
```

🔎 Output Preview
```python
Please enter a number: 2
5.0
```

---

## 💻 Program 2 — Try / Except / Else

This program prints the result only when conversion succeeds.

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That's not a number")
else:
    print(f"Thank you! Your number is: {number}")
```

🔎 Output Preview
```python
Enter a number: 8
Thank you! Your number is: 8
```

---

## 💻 Program 3 — Error Object

This program saves the exception into a variable and prints the message.

```python
try:
    x = int("abc")
except ValueError as e:
    print(f"Error: {e}")
```

🔎 Output Preview
```python
Error: invalid literal for int() with base 10: 'abc'
```

---

## 💻 Program 4 — Try / Except / Finally

This program always prints a final message.

```python
try:
    number = int(input("Enter a number: "))
    print(f"Your number: {number}")
except ValueError:
    print("That's not a number")
finally:
    print("Goodbye")
```

🔎 Output Preview
```python
Enter a number: hello
That's not a number
Goodbye
```

---

## 💻 Program 5 — Input Validation

This program checks for empty or invalid input before continuing.

```python
try:
    user_input = input("Enter a number: ")
    if user_input == "":
        raise TypeError

    number = int(user_input)
    print(f"You entered: {number}")
except (ValueError, TypeError):
    print("Invalid data type. Please enter a valid number.")
```

🔎 Output Preview
```python
Enter a number:
Invalid data type. Please enter a valid number.
```

---

## 💻 Program 6 — Specific Errors

This program handles invalid numbers and division by zero separately.

```python
try:
    number_input = int(input("Please enter a number: "))
    print(10 / number_input)
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

🔎 Output Preview
```python
Please enter a number: 0
Cannot divide by zero.
```

---

## 💻 Program 7 — Integer Validation

This program validates that the user entered an integer.

```python
try:
    user_input = input("Enter a number: ")
    number = int(user_input)
    print(f"You entered: {number}")
except ValueError:
    print("Please enter a valid integer.")
```

🔎 Output Preview
```python
Enter a number: text
Please enter a valid integer.
```

---

## 📂 Files in This Folder

```text
d09_try_except_basic
│
├── README.md
├── d09_task_01_division_with_input.py
├── d09_task_02_try_except_else.py
├── d09_task_03_error_object.py
├── d09_task_04_try_except_finally.py
├── d09_task_05_input_validation.py
├── d09_task_06_specific_errors.py
└── d09_task_07_integer_validation.py
```

Each file demonstrates a different way to handle basic errors in Python.
