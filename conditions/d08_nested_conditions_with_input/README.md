<p align="center">
  <img src="https://raw.githubusercontent.com/DataAstral/DataAstral/main/banner.png" width="100%">
</p>

# Welcome to DataAstral

One million projects. One path to mastery.

Progress: [░░░░░░░░░░] 0.0001% complete

---

## d08_nested_conditions_with_input

**Python Nested Conditions (`if inside if`) + User Input + `.lower()`**

This program demonstrates how to use nested conditions together with user input and normalize text using `.lower()`.

---

## What This Program Does

The program:

1. Asks the user to enter a username.
2. Asks the user to enter a password.
3. Converts input to lowercase using `.lower()`.
4. Checks if the username is correct.
5. If the username is correct, it checks the password.
6. Uses nested `if` statements to control the logic.
7. Displays different messages depending on the result.

---

## 💻 Python Code

```python
# Authentication system with user input

# Ask user to enter username
username = input("Enter username: ").lower()

# Ask user to enter password
password = input("Enter password: ").lower()

# Check username first
if username == "admin":
    # Then check password
    if password == "1234":
        print("Welcome!")
    else:
        print("Incorrect password")
else:
    print("User not found")
```

---

## 🔎 Output Preview

```python
Enter username: ADMIN
Enter password: 1234
Welcome!
```

```python
Enter username: admin
Enter password: 1111
Incorrect password
```

```python
Enter username: user
Enter password: 1234
User not found
```
