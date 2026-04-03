<p align="center">
  <img src="https://raw.githubusercontent.com/DataAstral/DataAstral/main/banner.png" width="100%">
</p>

# Welcome to DataAstral  
One million projects. One path to mastery.  

Progress: [░░░░░░░░░░] 0.0001% complete  

---

## d10_ternary_operator_even_odd

**Python Ternary Operator — Even or Odd Check**

This program demonstrates how to use a **ternary operator** to check whether a number is even or odd.

---

## What This Program Does

The program:

• asks the user to enter a number  
• converts the input into an integer using `int()`  
• checks if the number is divisible by 2  
• uses a **ternary operator** to decide the result  
• prints whether the number is “Even” or “Odd”  

---

## 💻 Python Code

```python
# Ask user for a number
number = int(input("Enter a number: "))

# Check if number is even or odd using ternary operator
result = "Even" if number % 2 == 0 else "Odd"

# Print result
print(result)
```

---

## 🔎 Output Preview

### ✅ Even number
```
Enter a number: 8
Even
```

### ❌ Odd number
```
Enter a number: 7
Odd
```

---

## Key Concept

- `%` (modulo) → returns the remainder of division  
- `number % 2 == 0` → means the number is even  
- ternary operator allows you to write conditions in one line  

Example:

```
"Even" if number % 2 == 0 else "Odd"
```

This is a compact way to replace a full `if/else` block.