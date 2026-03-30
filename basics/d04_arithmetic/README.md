<p align="center">
  <img src="https://raw.githubusercontent.com/DataAstral/DataAstral/main/banner.png" width="100%">
</p>

# Welcome to DataAstral

One million projects. One path to mastery.

Progress: [░░░░░░░░░░] 0.0001% complete

---

## d04_arithmetic_operations

**Python Arithmetic Operations (User Input + Math)**

This program demonstrates how to take numbers from the user and perform basic arithmetic operations.

---

## What This Program Does

The program:

1. Asks the user to enter two numbers.
2. Converts the input from text to integers using `int()`.
3. Performs different arithmetic operations.
4. Displays the results of each calculation.

---

## 💻 Python Code

```python
# Ask the user for the first number and convert it to integer
a = int(input("Enter the first number: "))

# Ask the user for the second number and convert it to integer
b = int(input("Enter the second number: "))

# Perform arithmetic operations and display results

# Addition
print("Addition:", a + b)

# Subtraction
print("Subtraction:", a - b)

# Multiplication
print("Multiplication:", a * b)

# Division (returns float)
print("Division:", a / b)

# Floor division (removes decimal part)
print("Floor division:", a // b)

# Modulus (remainder after division)
print("Remainder (modulus):", a % b)
```

---

## 🔎 Output Preview

```python
Enter the first number: 10
Enter the second number: 3

Addition: 13
Subtraction: 7
Multiplication: 30
Division: 3.3333333333333335
Floor division: 3
Remainder (modulus): 1
```

---

## Key Concepts

- `input()` → gets data from the user  
- `int()` → converts text to numbers  
- `+` → addition  
- `-` → subtraction  
- `*` → multiplication  
- `/` → division (float result)  
- `//` → floor division (integer result)  
- `%` → modulus (remainder)
