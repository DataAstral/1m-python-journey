<p align="center">
  <img src="https://raw.githubusercontent.com/DataAstral/DataAstral/main/banner.png" width="100%">
</p>

# Welcome to DataAstral

One million projects. One path to mastery.

Progress: [░░░░░░░░░░] 0.0001% complete

---

## d13_loops_range()

**Python For Loops (`for`, `range()`)**

This folder contains small Python programs that demonstrate how `for` loops and the `range()` function work in Python.

These programs show how to repeat actions, print number sequences, calculate squares, find numbers that match conditions, build totals, and create countdowns.

---

## What These Programs Do

These programs demonstrate:

• how to repeat code using `for`  
• how to generate sequences with `range()`  
• how to print numbers in order  
• how to use conditions inside loops  
• how to calculate squares and totals  
• how to count backward in a loop  

The examples gradually become slightly more complex.

---

## 💻 Program 1 — Study Python 5 Times

This program prints the sentence `I study Python` 5 times.

```python
# Print "I study Python" 5 times
for i in range(5):
    print("I study Python")
```

🔎 Output Preview
```python
I study Python
I study Python
I study Python
I study Python
I study Python
```

---

## 💻 Program 2 — Numbers from 1 to 10

This program prints numbers from 1 to 10.

```python
# Print numbers from 1 to 10
for i in range(1, 11):
    print(i)
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

## 💻 Program 3 — Numbers and Squares

This program prints numbers from 1 to 10 together with their squares.

```python
# Print numbers from 1 to 10 and their squares
for i in range(1, 11):
    print(i, i * i)
```

🔎 Output Preview
```python
1 1
2 4
3 9
4 16
...
10 100
```

---

## 💻 Program 4 — Even Numbers from 1 to 20

This program prints only even numbers from 1 to 20.

```python
# Print even numbers from 1 to 20
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
```

🔎 Output Preview
```python
2
4
6
8
...
20
```

---

## 💻 Program 5 — Numbers Divisible by 3

This program prints numbers from 1 to 30 that are divisible by 3.

```python
# Print numbers from 1 to 30 that are divisible by 3
for i in range(1, 31):
    if i % 3 == 0:
        print(i)
```

🔎 Output Preview
```python
3
6
9
12
...
30
```

---

## 💻 Program 6 — Sum from 1 to 50

This program calculates the sum of numbers from 1 to 50.

```python
# Calculate the sum of numbers from 1 to 50
total = 0

for i in range(1, 51):
    total += i

print(total)
```

🔎 Output Preview
```python
1275
```

---

## 💻 Program 7 — Countdown from 10 to 1

This program prints a countdown from 10 to 1.

```python
# Print a countdown from 10 to 1
for i in range(10, 0, -1):
    print(i)
```

🔎 Output Preview
```python
10
9
8
7
...
1
```

---

## 📂 Files in This Folder

```text
d13_loops_range()
│
├── d13_task_01_study_python_5_times.py
├── d13_task_02_numbers_1_to_10.py
├── d13_task_03_numbers_and_squares.py
├── d13_task_04_even_numbers_1_to_20.py
├── d13_task_05_numbers_divisible_by_3.py
├── d13_task_06_sum_1_to_50.py
├── d13_task_07_countdown_10_to_1.py
└── README.md
```

Each file demonstrates a different way of using `for` loops and `range()` in Python.
