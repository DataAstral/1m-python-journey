<p align="center">
  <img src="https://raw.githubusercontent.com/DataAstral/DataAstral/main/banner.png" width="100%">
</p>

# Welcome to DataAstral

One million projects. One path to mastery.

Progress: [░░░░░░░░░░] 0.0001% complete

---

## d08_nested_conditions_discount_system

**Python Nested Conditions (`if inside if`) — Decision Logic**

This program demonstrates how to use nested conditions to apply different outcomes based on multiple levels of checks.

---

## What This Program Does

The program:

1. Stores user data (age and membership status).
2. First checks if the user is an adult.
3. If the user is an adult, it checks if they are a member.
4. Uses nested `if` statements to control decision flow.
5. Displays different messages depending on the result.

---

## 💻 Python Code

```python
# Discount system with nested conditions

age = 20
is_member = True

# Check if the user is an adult
if age >= 18:
    # Check membership status
    if is_member:
        print("20% discount for members")
    else:
        print("No discount, but you are an adult")
else:
    print("Adults only")
```

---

## 🔎 Output Preview

```python
20% discount for members
```

```python
No discount, but you are an adult
```

```python
Adults only
```
