<p align="center">
  <img src="https://raw.githubusercontent.com/DataAstral/DataAstral/main/banner.png" width="100%">
</p>

# Welcome to DataAstral

One million projects. One path to mastery.

Progress: [░░░░░░░░░░] 0.0001% complete

---

## d07_logical_operators

**Python Logical Operators (`and`, `or`, `not`)**

This folder contains small Python programs that demonstrate how logical operators work in Python.

These programs show how to combine rules, validate several conditions at once, and control access with grouped logic.

---

## What These Programs Do

These programs demonstrate:

• how to combine conditions with `and`  
• how to allow alternative conditions with `or`  
• how to reverse logic with `not`  
• how to use parentheses for clearer condition grouping  

The examples gradually become slightly more complex.

---

## 💻 Program 1 — Access with Password or Token

This program checks age together with password or token access.

```python
age = int(input("Enter your age: "))
password = input("Do you know the password? (yes/no): ")
token = input("Do you have a token? (yes/no): ")

has_password = password == "yes"
has_token = token == "yes"

if age >= 18 and (has_password or has_token):
    print("Access granted")
else:
    print("Access denied")
```

🔎 Output Preview
```python
Enter your age: 22
Do you know the password? (yes/no): no
Do you have a token? (yes/no): yes
Access granted
```

---

## 💻 Program 2 — Travel Check

This program uses `and` to require two true conditions.

```python
passport = input("Do you have a passport? (yes/no): ")
visa = input("Do you have a visa? (yes/no): ")

if passport == "yes" and visa == "yes":
    print("You can travel abroad!")
else:
    print("You cannot travel.")
```

🔎 Output Preview
```python
Do you have a passport? (yes/no): yes
Do you have a visa? (yes/no): yes
You can travel abroad!
```

---

## 💻 Program 3 — Exam Check

This program checks two user inputs at the same time.

```python
print("Let's check your results!")
test = input("Did you pass your test (yes/no): ")
on_time = input("Did you arrive on time (yes/no): ")

if test.lower() == "yes" and on_time.lower() == "yes":
    print("Exam passed")
else:
    print("Exam failed")
```

🔎 Output Preview
```python
Let's check your results!
Did you pass your test (yes/no): yes
Did you arrive on time (yes/no): no
Exam failed
```

---

## 💻 Program 4 — Logical Precedence

This program demonstrates how parentheses affect `and` and `or`.

```python
age = 20
has_ticket = True
is_vip = False

if (age >= 18 and has_ticket) or is_vip:
    print("Welcome!")
else:
    print("Access denied.")
```

🔎 Output Preview
```python
Welcome!
```

---

## 📂 Files in This Folder

```text
d07_logical_operators
│
├── README.md
├── d07_task_01_access_with_password_or_token.py
├── d07_task_02_travel_check.py
├── d07_task_03_exam_check.py
└── d07_task_04_logical_precedence.py
```

Each file demonstrates a different way to use `and`, `or`, and `not`.
