<p align="center">
  <img src="https://raw.githubusercontent.com/DataAstral/DataAstral/main/banner.png" width="100%">
</p>

# Welcome to DataAstral

One million projects. One path to mastery.

Progress: [░░░░░░░░░░] 0.0001% complete

---

## d07_logical_operators_precedence

**Python Logical Operators + Condition Grouping (`and`, `or`, parentheses)**

This program demonstrates how Python evaluates complex logical expressions using operator precedence and grouping.

---

## What This Program Does

The program:

1. Stores user data (age, ticket, VIP status).
2. Uses a complex condition with `and` and `or`.
3. Applies parentheses to control logic priority.
4. Grants access if:
   - The user is 18+ AND has a ticket  
   - OR the user is a VIP  
5. Demonstrates how grouping changes program behavior.

---

## 💻 Python Code

```python
# Access control with logical grouping

age = 20
has_ticket = True
is_vip = False

# Access logic with parentheses
if (age >= 18 and has_ticket) or is_vip:
    print("Welcome!")
else:
    print("Access denied.")
```

---

## 🔎 Output Preview

```python
Welcome!
```
