<p align="center">
  <img src="https://raw.githubusercontent.com/DataAstral/DataAstral/main/banner.png" width="100%">
</p>

# Welcome to DataAstral

One million projects. One path to mastery.

Progress: [░░░░░░░░░░] 0.0001% complete

---

## d11_loops_while

**Python While Loops (`while`, `break`, `else`)**

This folder contains small Python programs that demonstrate how `while` loops work in Python.

These programs show how to repeat actions, ask for user input many times, stop loops with conditions, and control loop behavior with `break` and `else`.

---

## What These Programs Do

These programs demonstrate:

• how to repeat code using `while`  
• how to stop a loop when a condition changes  
• how to use `break` to exit a loop  
• how to work with user input inside loops  
• how to count attempts  
• how to build simple interactive programs  

The examples gradually become slightly more complex.

---

## 💻 Program 1 — Counter

This program prints numbers from 1 to 5 using a `while` loop.

```python
# task_01_counter.py
counter = 1
while counter <= 5:
    print(f" Number: {counter}")
    counter += 1
print ("The cycle is over!")
```

🔎 Output Preview
```python
 Number: 1
 Number: 2
 Number: 3
 Number: 4
 Number: 5
The cycle is over!
```

---

## 💻 Program 2 — Password Check

This program keeps asking for a password until the correct password is entered.

```python
# task_02_password.py
password = ""
while password != "123456789":
    password = input("Enter your password: ")
    if password == "123456789":
        print("Password is correct")
    else:
        print("Password is incorrect")
```

🔎 Output Preview
```python
Enter your password: 123
Password is incorrect
Enter your password: 123456789
Password is correct
```

---

## 💻 Program 3 — Timer

This program counts down from 9 to 0.

```python
# task_03_timer.py
time = 10
while time > 0:
    time = time - 1
    print(f"Time left: {time}")
```

🔎 Output Preview
```python
Time left: 9
Time left: 8
Time left: 7
...
Time left: 0
```

---

## 💻 Program 4 — Numbers from 1 to 10

This program prints numbers from 1 to 10 in a column.

```python
# task_04_numbers_1_to_10.py
number = 0
while number < 10:
    number += 1
    print(number)
```

🔎 Output Preview
```python
1
2
3
4
5
...
10
```

---

## 💻 Program 5 — Input Until Zero

This program keeps asking the user for numbers until the user enters `0`.

```python
# task_05_input_until_zero.py
user_input = int(input("Enter a number: "))
while user_input != 0:
    print("You entered", user_input)
    user_input = int(input("Enter a number: "))
print("Thank you for your time")
```

🔎 Output Preview
```python
Enter a number: 5
You entered 5
Enter a number: 8
You entered 8
Enter a number: 0
Thank you for your time
```

---

## 💻 Program 6 — Password Attempts

This program gives the user 3 attempts to enter the correct password.

```python
# task_06_password_attempts.py
attempts = 3
while attempts > 0:
    user_password = input("Enter your password: ")
    if user_password == "admin123":
        print("Welcome")
        break
    else:
        attempts -= 1
        print("Password is incorrect.")
if attempts == 0:
    print("Blocked")
```

🔎 Output Preview
```python
Enter your password: test
Password is incorrect.
Enter your password: hello
Password is incorrect.
Enter your password: admin123
Welcome
```

---

## 💻 Program 7 — Guessing Game with Attempts

This program lets the user guess a secret number with a limited number of attempts.

```python
# task_07_guess_with_attempts.py
attempts = 5
while attempts > 0:
    try:
        number_input = int(input("Enter a number: "))
        if number_input == 7:
            print("Correct")
            break
        else:
            attempts -= 1
            print("Try again!")
    except ValueError:
        print("Only numbers are accepted.")
if attempts == 0:
    print("Game over")
```

🔎 Output Preview
```python
Enter a number: hello
Only numbers are accepted.
Enter a number: 3
Try again!
Enter a number: 7
Correct
```

---

## 💻 Program 8 — Infinite Guessing Game

This program keeps asking the user to guess the secret number until the answer is correct.

```python
# task_08_guess_infinite.py
secret_number = 7
while True:
    question = int(input("Try to guess my number: "))
    if question == 7:
        print("You guessed my number is 7")
        break
    elif question > 7:
        print("You guessed too high")
    else:
        print("You guessed too low")
```

🔎 Output Preview
```python
Try to guess my number: 10
You guessed too high
Try to guess my number: 4
You guessed too low
Try to guess my number: 7
You guessed my number is 7
```

---

## 💻 Program 9 — Guessing Game with `else`

This program gives the user 5 attempts to guess the secret number and uses `else` if all attempts are over.

```python
# task_09_guess_with_else.py
attempts = 0
secret_number = 7
while attempts < 5:
    attempts = attempts + 1
    question = int(input("Try to guess my number: "))
    if question == secret_number:
        print("You guessed my number is 7")
        break
    elif question > secret_number:
        print("You guessed too high")
    else:
        print("You guessed too low")
else:
    print("Your attempts are over!")
```

🔎 Output Preview
```python
Try to guess my number: 1
You guessed too low
Try to guess my number: 2
You guessed too low
Try to guess my number: 3
You guessed too low
Try to guess my number: 4
You guessed too low
Try to guess my number: 5
You guessed too low
Your attempts are over!
```

---

## 💻 Program 10 — Bank Balance Menu

This program creates a simple bank menu that works in an infinite loop until the user exits.

```python
# task_10_bank_balance.py
balance = 1000

while True:
    print("\n--- BANK MENU ---")
    print("1. Check balance")
    print("2. Deposit money")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print(f"Your balance is: {balance}$")

    elif choice == "2":
        print("Deposit function is under development...")

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Error! Please enter a valid option.")
```

🔎 Output Preview
```python
--- BANK MENU ---
1. Check balance
2. Deposit money
0. Exit
Choose an option: 1
Your balance is: 1000$

--- BANK MENU ---
1. Check balance
2. Deposit money
0. Exit
Choose an option: 0
Goodbye!
```

---

## 📂 Files in This Folder

```text
d11_loops_while
│
├── d11_task_01_counter.py
├── d11_task_02_password.py
├── d11_task_03_timer.py
├── d11_task_04_numbers_1_to_10.py
├── d11_task_05_input_until_zero.py
├── d11_task_06_password_attempts.py
├── d11_task_07_guess_with_attempts.py
├── d11_task_08_guess_infinite.py
├── d11_task_09_guess_with_else.py
├── task_10_bank_balance.py
└── README.md
```

Each file demonstrates a different way of using `while` loops in Python.
