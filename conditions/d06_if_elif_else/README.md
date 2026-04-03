<p align="center">
  <img src="https://raw.githubusercontent.com/DataAstral/DataAstral/main/banner.png" width="100%">
</p>

# Welcome to DataAstral

One million projects. One path to mastery.

Progress: [░░░░░░░░░░] 0.0001% complete

---

## d06_if_elif_else

**Python Conditions (`if`, `elif`, `else`)**

This folder contains small Python programs that demonstrate how conditional statements work in Python.

These programs show how to compare values, branch between multiple outcomes, and build simple decision-making logic.

---

## What These Programs Do

These programs demonstrate:

• how to use `if` and `else` for basic decisions  
• how to use `elif` for multiple cases  
• how to compare numbers and text  
• how to combine simple conditions in one program  

The examples gradually become slightly more complex.

---

## 💻 Program 1 — Age Access Check

This program asks the user for their age and decides whether access is allowed.

```python
age_input = input("Enter your age: ")
age = int(age_input)

if age >= 18:
    print("Welcome to the website!")
else:
    years_left = 18 - age
    print("Too early. Come back in", years_left, "years.")
```

🔎 Output Preview
```python
Enter your age: 16
Too early. Come back in 2 years.
```

---

## 💻 Program 2 — Mood Checker

This program uses `if`, `elif`, and `else` to react to the user's mood.

```python
mood = input("What is your mood? (happy/sad/other): ")

if mood == "happy":
    print("Keep smiling!")
elif mood == "sad":
    print("Don't worry, be happy!")
else:
    print("Have a good day anyway!")
```

🔎 Output Preview
```python
What is your mood? (happy/sad/other): happy
Keep smiling!
```

---

## 💻 Program 3 — Multiple Cases

This program checks a status code and prints a different result for each case.

```python
status_code = 404

if status_code == 200:
    print("OK - request successful")
elif status_code == 404:
    print("Not Found - resource not found")
elif status_code == 500:
    print("Server Error - internal server error")
else:
    print(f"Unknown status: {status_code}")
```

🔎 Output Preview
```python
Not Found - resource not found
```

---

## 💻 Program 4 — Access Control

This program combines age and ticket checks in one decision.

```python
age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("Welcome!")
elif age >= 18 and not has_ticket:
    print("You need a ticket.")
else:
    print("Access denied: you are under 18.")
```

🔎 Output Preview
```python
Welcome!
```

---

## 📂 Files in This Folder

```text
d06_if_elif_else
│
├── README.md
├── d06_task_01_age_access_check.py
├── d06_task_02_mood_checker.py
├── d06_task_03_multiple_cases.py
└── d06_task_04_access_control.py
```

Each file demonstrates a different way to work with `if`, `elif`, and `else`.
