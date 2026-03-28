<p align="center">
  <img src="https://raw.githubusercontent.com/DataAstral/DataAstral/main/banner.png" width="100%">
</p>
# Welcome to DataAstral

One million projects. One path to mastery.

Progress: [░░░░░░░░░░] 0.0001% complete

---

# **⌨️** d04_comparison_and_logic

## ⚙️ Topic

**Comparison Operators & Logical Expressions in Python**

This program demonstrates how Python compares values and evaluates logical conditions.

---

# 🧠 What This Program Does

The program:

1. Asks the user to enter two numbers.
2. Compares these numbers using different comparison operators.
3. Evaluates logical conditions using `and`, `or`, and `not`.
4. Prints the results of each comparison and logical expression.

---

# 💻 Python Code

```python
# Ask the user for two numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Comparison operators
print("a == b:", a == b)   # Check if a is equal to b
print("a != b:", a != b)   # Check if a is not equal to b
print("a > b:", a > b)     # Check if a is greater than b
print("a < b:", a < b)     # Check if a is less than b
print("a >= b:", a >= b)   # Check if a is greater than or equal to b
print("a <= b:", a <= b)   # Check if a is less than or equal to b

# Logical expressions
print("Both are positive:", a > 0 and b > 0)        # True if both numbers are positive
print("At least one is positive:", a > 0 or b > 0) # True if at least one number is positive
print("a is not positive:", not (a > 0))           # True if a is NOT positive
```

---

# 🔎 Output Preview

```python
Enter the first number: 5
Enter the second number: -3

a == b: False
a != b: True
a > b: True
a < b: False
a >= b: True
a <= b: False

Both are positive: False
At least one is positive: True
a is not positive: False
```
