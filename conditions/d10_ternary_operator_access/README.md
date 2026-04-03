<p align="center">
  <img src="https://raw.githubusercontent.com/DataAstral/DataAstral/main/banner.png" width="100%">
</p>

# Welcome to DataAstral  
One million projects. One path to mastery.  

Progress: [░░░░░░░░░░] 0.0001% complete  

---

## d10_ternary_operator_access

**Python Ternary Operator — Conditional Expression**

This program demonstrates how to use a **ternary operator** to make decisions in a short and clean way.

---

## What This Program Does

The program:

• asks the user to enter their age  
• converts the input into an integer using `int()`  
• checks if the age is 18 or older  
• uses a **ternary operator** to decide the result  
• prints either “Access granted” or “Access denied”  

---

## 💻 Python Code

```python
# Ask user for age
age = int(input("Enter your age: "))

# Use ternary operator to decide access
result = "Access granted" if age >= 18 else "Access denied"

# Print result
print(result)
```

---

## 🔎 Output Preview

### ✅ Adult
```
Enter your age: 20
Access granted
```

### ❌ Underage
```
Enter your age: 16
Access denied
```

---

## Key Concept

- `condition ? true : false` → ❌ (NOT Python)  
- Python way:

```
value_if_true if condition else value_if_false
```

Example:

```
"Access granted" if age >= 18 else "Access denied"
```

This is a shorter alternative to `if/else` and is often used in clean, professional code.
