<p align="center">
  <img src="https://raw.githubusercontent.com/DataAstral/DataAstral/main/banner.png" width="100%">
</p>

# Welcome to DataAstral

One million projects. One path to mastery.

Progress: [░░░░░░░░░░] 0.0001% complete

---

## d08_nested_conditions

**Python Nested Conditions (`if` inside `if`)**

This folder contains small Python programs that demonstrate how nested conditions work in Python.

These programs show how to check one rule inside another rule and build multi-step decision-making programs.

---

## What These Programs Do

These programs demonstrate:

• how to place one `if` inside another  
• how to validate input step by step  
• how to build multi-level access logic  
• how to separate full, partial, and denied access  

The examples gradually become slightly more complex.

---

## 💻 Program 1 — Discount System

This program checks age first and then membership status.

```python
age = 20
is_member = True

if age >= 18:
    if is_member:
        print("20% discount for members")
    else:
        print("No discount, but you are an adult")
else:
    print("Adults only")
```

🔎 Output Preview
```python
20% discount for members
```

---

## 💻 Program 2 — Login Check

This program checks the username first and then the password.

```python
username = input("Enter username: ").lower()
password = input("Enter password: ").lower()

if username == "admin":
    if password == "1234":
        print("Welcome!")
    else:
        print("Incorrect password")
else:
    print("User not found")
```

🔎 Output Preview
```python
Enter username: admin
Enter password: 1234
Welcome!
```

---

## 💻 Program 3 — Security System

This program uses three levels of nested checks for access control.

```python
age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (yes/no): ").lower() == "yes"
knows_code = input("Do you know the security code? (yes/no): ").lower() == "yes"

if age >= 18:
    if has_id:
        if knows_code:
            print("Full access granted")
        else:
            print("Partial access: ID confirmed, but security code is missing")
    else:
        print("Access denied: ID card required")
else:
    print("Access denied: adults only")
```

🔎 Output Preview
```python
Enter your age: 21
Do you have an ID? (yes/no): yes
Do you know the security code? (yes/no): no
Partial access: ID confirmed, but security code is missing
```

---

## 📂 Files in This Folder

```text
d08_nested_conditions
│
├── README.md
├── d08_task_01_discount_system.py
├── d08_task_02_login_check.py
└── d08_task_03_security_system.py
```

Each file demonstrates a different way to build nested condition logic.
