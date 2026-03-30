<p align="center">
  <img src="https://raw.githubusercontent.com/DataAstral/DataAstral/main/banner.png" width="100%">
</p>

# Welcome to DataAstral

One million projects. One path to mastery.

Progress: [░░░░░░░░░░] 0.0001% complete

---

## d08_nested_conditions_with_input_system

**Python Nested Conditions (`if inside if`) + User Input + Boolean Logic**

This program demonstrates how to build a multi-step decision system using nested conditions and user input.

---

## What This Program Does

The program:

1. Asks the user for their age.
2. Asks if the user has an ID.
3. Asks if the user knows the security code.
4. Converts user input into boolean values.
5. Uses nested `if` statements (3 levels deep).
6. Determines access level:
   - Full access  
   - Partial access  
   - Access denied  

---

## 💻 Python Code

```python
# 🔐 Security access system with user input

# Ask the user for their age
age = int(input("Enter your age: "))

# Ask if the user has an ID
has_id_input = input("Do you have an ID? (yes/no): ")

# Ask if the user knows the security code
knows_code_input = input("Do you know the security code? (yes/no): ")

# Convert answers to boolean values
has_id = has_id_input.lower() == "yes"
knows_code = knows_code_input.lower() == "yes"

# First check: is the user an adult?
if age >= 18:
    # Second check: does the user have an ID?
    if has_id:
        # Third check: does the user know the security code?
        if knows_code:
            print("Full access granted")
        else:
            print("Partial access: ID confirmed, but security code is missing")
    else:
        # User is adult, but has no ID
        print("Access denied: ID card required")
else:
    # User is under 18
    print("Access denied: adults only")
```

---

## 🔎 Output Preview

```python
Enter your age: 20
Do you have an ID? (yes/no): yes
Do you know the security code? (yes/no): yes
Full access granted
```

```python
Enter your age: 20
Do you have an ID? (yes/no): yes
Do you know the security code? (yes/no): no
Partial access: ID confirmed, but security code is missing
```

```python
Enter your age: 20
Do you have an ID? (yes/no): no
Do you know the security code? (yes/no): no
Access denied: ID card required
```

```python
Enter your age: 16
Do you have an ID? (yes/no): yes
Do you know the security code? (yes/no): yes
Access denied: adults only
```
