<p align="center">
  <img src="https://raw.githubusercontent.com/DataAstral/DataAstral/main/banner.png" width="100%">
</p>

# Welcome to DataAstral  
One million projects. One path to mastery.  

Progress: [░░░░░░░░░░] 0.0001% complete  

---

## d09_try_except_finally

**Python Error Handling — try / except / finally**

This program demonstrates how to handle user input safely and always execute final code using the `finally` block.

---

### What This Program Does

The program:

1. Asks the user to enter a number  
2. Tries to convert the input into an integer using `int()`  
3. If the input is invalid → catches the error (`ValueError`)  
4. Prints the number if conversion is successful  
5. Always runs the `finally` block → prints a goodbye message  

---

## 💻 Python Code

```python
# Try to get a number from the user
try:
    number = int(input("Enter a number: "))
    print(f"Your number: {number}")

# Handle error if input is not a number
except ValueError:
    print("That's not a number")

# This block always runs
finally:
    print("Goodbye")
```

---

## 🔎 Output Preview

### ✅ Valid input
```
Enter a number: 10
Your number: 10
Goodbye
```

### ❌ Invalid input
```
Enter a number: hello
That's not a number
Goodbye
```

---

### Key Concept

- `try` → code that may cause an error  
- `except` → handles the error  
- `finally` → always runs (even if an error happens)  

This is useful for cleanup actions like:
- closing files  
- saving data  
- showing final messages  

This makes your programs **reliable and professional**.