# Welcome to DataAstral

One million projects. One path to mastery.

Progress: [░░░░░░░░░░] 0.0001% complete

---

# ⌨️ d03_input_basic

## ⚙️ Topic

**Python User Input (`input()` function)**

This folder contains small Python programs that demonstrate how to receive input from a user and use it inside a program.

User input is one of the most important basics in programming because it allows programs to interact with people.

---

# 🧠 What These Programs Do

These programs demonstrate:

• how to ask the user to type text  
• how to store user input in variables  
• how to print the information back to the screen  
• how to convert input into different data types  

The examples gradually become slightly more complex.

---

# 💻 Program 1 — Basic Input

This program asks the user to type something and then prints the same text.

```python
# Ask the user to type something
user_input = input("Type something: ")

# Show the same text back to the user
print("You typed:", user_input)
```

---

# 💻 Program 2 — Greeting Program

This program asks the user for their name and greets them.

```python
# Program for greeting
name = input("Your name: ")
print("Hello,", name)
```

---

# 💻 Program 3 — Name and Age Input

This program asks the user for their name and age, then prints a message.

```python
# Welcome message
print("Welcome to my Python program!")

# Ask the user for their name
name = input("What is your name? ")

# Ask the user for their age
age = input("How old are you? ")

# Show the result
print("Hello", name, "you are", age, "years old.")
```

---

# 💻 Program 4 — Input Data Types

This program demonstrates how user input can be converted into different data types.

```python
# Ask the user to enter a number
number = int(input("Enter a whole number: "))

# Ask the user to enter a decimal number
decimal = float(input("Enter a decimal number: "))

# Ask the user to enter text
text = input("Enter any text: ")

# Ask the user to enter True or False
boolean = bool(input("Enter True or False: "))

# Show the results
print("Integer:", number)
print("Float:", decimal)
print("String:", text)
print("Boolean:", boolean)
```

---

# 📂 Files in This Folder

```
d03_input_basic
│
├── input_basic.py
├── greeting_program.py
├── name_age_input.py
└── input_data_types.py
```

Each file demonstrates a slightly different way of working with the `input()` function.
