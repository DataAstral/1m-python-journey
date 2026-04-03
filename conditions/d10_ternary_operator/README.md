<p align="center">
  <img src="https://raw.githubusercontent.com/DataAstral/DataAstral/main/banner.png" width="100%">
</p>

# Welcome to DataAstral

One million projects. One path to mastery.

Progress: [░░░░░░░░░░] 0.0001% complete

---

## d10_ternary_operator

**Python Ternary Operator (`value_if_true if condition else value_if_false`)**

This folder contains small Python programs that demonstrate how ternary expressions work in Python.

These programs show how to write short conditional expressions, classify values, and combine ternary logic with validation and error handling.

---

## What These Programs Do

These programs demonstrate:

• how to replace simple `if / else` with a ternary operator  
• how to classify numbers and text in one line  
• how to chain multiple ternary expressions  
• how to combine ternary logic with `try` / `except`  

The examples gradually become slightly more complex.

---

## 💻 Program 1 — Access Check

This program uses a ternary operator to decide access by age.

```python
age = int(input("Enter your age: "))
result = "Access granted" if age >= 18 else "Access denied"
print(result)
```

🔎 Output Preview
```python
Enter your age: 19
Access granted
```

---

## 💻 Program 2 — Even or Odd

This program classifies a number as even or odd.

```python
number = int(input("Enter a number: "))
result = "Even" if number % 2 == 0 else "Odd"
print(result)
```

🔎 Output Preview
```python
Enter a number: 7
Odd
```

---

## 💻 Program 3 — Even or Odd with Error Handling

This program keeps the ternary operator but adds `try` / `except`.

```python
try:
    number = int(input("Enter a number: "))
    result = "Even" if number % 2 == 0 else "Odd"
    print(result)
except ValueError:
    print("Please enter a number")
```

🔎 Output Preview
```python
Enter a number: hello
Please enter a number
```

---

## 💻 Program 4 — Even or Odd with `else`

This program prints the result only after successful input conversion.

```python
try:
    number = int(input("Enter a number: "))
    result = "Even" if number % 2 == 0 else "Odd"
except ValueError:
    print("Please enter a number")
else:
    print(f"You entered {number} your result is {result}")
```

🔎 Output Preview
```python
Enter a number: 12
You entered 12 your result is Even
```

---

## 💻 Program 5 — Mood Checker

This program uses chained ternary expressions for three outcomes.

```python
mood = input("What is your mood?: (happy, sad, ok): ")
result = "happy" if mood == "happy" else "sad" if mood == "sad" else "ok"
print(f"Your mood is {result}")
```

🔎 Output Preview
```python
What is your mood?: (happy, sad, ok): sad
Your mood is sad
```

---

## 💻 Program 6 — Temperature Check

This program uses a ternary operator together with input validation.

```python
temperature = input("What is the temperature? (hot, warm, cold): ").lower()

if temperature in ("hot", "warm", "cold"):
    result = "Hot" if temperature == "hot" else "Cold" if temperature == "cold" else "Warm"
    print(result)
else:
    print("Please enter only: hot, warm, or cold")
```

🔎 Output Preview
```python
What is the temperature? (hot, warm, cold): warm
Warm
```

---

## 📂 Files in This Folder

```text
d10_ternary_operator
│
├── README.md
├── d10_task_01_access_check.py
├── d10_task_02_even_or_odd.py
├── d10_task_03_even_or_odd_safe.py
├── d10_task_04_even_or_odd_try_else.py
├── d10_task_05_mood_checker.py
└── d10_task_06_temperature_check.py
```

Each file demonstrates a different way to use the ternary operator in Python.
