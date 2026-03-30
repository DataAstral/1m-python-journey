<p align="center">
  <img src="https://raw.githubusercontent.com/DataAstral/DataAstral/main/banner.png" width="100%">
</p>
# Welcome to DataAstral

One million projects. One path to mastery.

Progress: [░░░░░░░░░░] 0.0001% complete

---

# **🔐** d06_conditions_and_logical_operators

**Python Conditions + Logical Operators (`and`, `not`)**

This program demonstrates how to control access using conditions based on age and ticket availability.

---

# What This Program Does

The program:

1. Stores user data (age and ticket status).
2. Checks if the user is allowed to enter.
3. Uses logical operators to combine conditions.
4. Displays different messages depending on the situation.

---

# 💻 Python Code

```python
# Access control system

# Store user data
age = 20
has_ticket = True

# Check access conditions
if age >= 18 and has_ticket:
    print("Welcome!")
elif age >= 18 and not has_ticket:
    print("You need a ticket.")
else:
    print("Access denied: you are under 18.")
```

---

# 🔎 Output Preview

```python
Welcome!
```
