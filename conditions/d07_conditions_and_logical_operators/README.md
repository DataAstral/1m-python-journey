<p align="center">
  <img src="https://raw.githubusercontent.com/DataAstral/DataAstral/main/banner.png" width="100%">
</p>

# Welcome to DataAstral

One million projects. One path to mastery.

Progress: [░░░░░░░░░░] 0.0001% complete

---

## d07_conditions_and_logical_operators

**Python Conditions + Logical Operators (`and`, `or`)**

This program demonstrates how to combine multiple conditions using logical operators to control access.

---

##  What This Program Does

The program:

1. Asks the user for their age.
2. Asks if the user knows the password.
3. Asks if the user has a token.
4. Uses `and` and `or` to combine conditions.
5. Grants access only if:
   - The user is 18 or older  
   - AND has either a password OR a token  

---

## 💻 Python Code

```python
# Access control system

# Ask the user for their age
age = int(input("Enter your age: "))

# Ask if the user knows the password
password = input("Do you know the password? (yes/no): ")

# Ask if the user has a token
token = input("Do you have a token? (yes/no): ")

# Check conditions
has_password = password == "yes"
has_token = token == "yes"

# Access logic
if age >= 18 and (has_password or has_token):
    print("✅ Access granted")
else:
    print("❌ Access denied")
```

---

## 🔎 Output Preview

```python
Enter your age: 20
Do you know the password? (yes/no): yes
Do you have a token? (yes/no): no
✅ Access granted
```

```python
Enter your age: 16
Do you know the password? (yes/no): no
Do you have a token? (yes/no): no
❌ Access denied
```

```python
Enter your age: 20
Do you know the password? (yes/no): no
Do you have a token? (yes/no): no
❌ Access denied
```
