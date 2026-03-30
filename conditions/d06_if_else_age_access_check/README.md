<p align="center">
  <img src="https://raw.githubusercontent.com/DataAstral/DataAstral/main/banner.png" width="100%">
</p>
# Welcome to DataAstral

One million projects. One path to mastery.

Progress: [░░░░░░░░░░] 0.0006% complete

---

# **⌨️** d06_if_else_age_access_check

**Python Conditions (if / else statements)**

This program demonstrates how Python can make decisions based on user input.

---

# What This Program Does

The program:

1. Asks the user to enter their age.
2. Converts the input from text to a number.
3. Checks if the user is 18 or older.
4. If yes — access is granted.
5. If not — the program calculates how many years are left until 18.

---

# 💻 Python Code

```python
# Ask the user to enter their age (as a string)
age_input = input("Enter your age: ")

# Convert the input into an integer
age = int(age_input)

# Check the condition: if age is 18 or older — access is allowed
if age >= 18:
    print("Welcome to the website!")
# Otherwise, calculate how many years are left until 18
else:
    years_left = 18 - age
    print("Too early. Come back in", years_left, "years.")
```

---

# 🔎 Output Preview

```python
Enter your age: 16
Too early. Come back in 2 years.
```

```python
Enter your age: 21
Welcome to the website!
```