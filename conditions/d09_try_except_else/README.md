<p align="center">
  <img src="https://raw.githubusercontent.com/DataAstral/DataAstral/main/banner.png" width="100%">
</p>

# Welcome to DataAstral  
One million projects. One path to mastery.  

Progress: [░░░░░░░░░░] 0.0001% complete  

---

##  d09_try_except_else

**Python Error Handling — try / except / else**

This program demonstrates how to safely handle user input and avoid crashes using exception handling.

---

###  What This Program Does

The program:

1. Asks the user to enter a number  
2. Tries to convert the input into an integer using `int()`  
3. If the user enters invalid data → catches the error (`ValueError`)  
4. If no error occurs → executes the `else` block  
5. Displays a confirmation message with the entered number  

---

## 💻 Python Code

```python
# Try to get a number from the user
try:
    number = int(input("Enter a number: "))

# Handle error if input is not a number
except ValueError:
    print("That's not a number")

# If no error happened, run this block
else:
    print(f"Thank you! Your number is: {number}")
```

---

## 🔎 Output Preview

### ✅ Valid input
```
Enter a number: 5
Thank you! Your number is: 5
```

### ❌ Invalid input
```
Enter a number: hello
That's not a number
```

---

###  Key Concept

- `try` → code that may cause an error  
- `except` → handles the error  
- `else` → runs only if no error occurred  

This structure helps you write **safe and professional programs** that don’t crash.

