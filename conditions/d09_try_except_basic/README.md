<p align="center">
  <img src="https://raw.githubusercontent.com/DataAstral/DataAstral/main/banner.png" width="100%">
</p>

# Welcome to DataAstral

One million projects. One path to mastery.

Progress: [░░░░░░░░░░] 0.0001% complete

---

## d09_try_except_basic

**Python Error Handling (try / except basics)**

This program demonstrates how to handle runtime errors using a simple `try` and `except` block.

---

## What This Program Does

The program:

1. Asks the user to enter a number.
2. Converts the input into an integer using `int()`.
3. Attempts to divide 10 by the entered number.
4. Prevents the program from crashing if an error occurs.
5. Displays a fallback message if something goes wrong.

---

## ⚠️ Important Note

In this example, we use a **bare `except`**, which catches **all possible errors**.

❗ This is **not recommended in real-world programming**, because:
- It hides the exact problem.
- It makes debugging harder.
- It can catch unexpected errors silently.

✅ However, this is **completely fine for learning purposes**,  
because right now you are focusing on understanding the concept of error handling.

Later, you will learn how to catch **specific errors** like:
- `ValueError`
- `ZeroDivisionError`

---

## 💻 Python Code

```python
# Try to execute code that may cause an error
try:
    # Ask the user to enter a number
    number_input = int(input("Please enter a number: "))
    
    # Attempt to divide 10 by the entered number
    print(10 / number_input)

# Catch any error (not recommended in real projects)
except:
    # Show a fallback message if something goes wrong
    print("Please enter a number")
```

---

## 🔎 Output Preview

```python
Please enter a number: 2
5.0
```

```python
Please enter a number: 0
Please enter a number
```

```python
Please enter a number: hello
Please enter a number
```
