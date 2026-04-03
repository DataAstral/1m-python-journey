<p align="center">
  <img src="https://raw.githubusercontent.com/DataAstral/DataAstral/main/banner.png" width="100%">
</p>

# Welcome to DataAstral

One million projects. One path to mastery.

Progress: [░░░░░░░░░░] 0.0001% complete

---

## d12_loops_for

**Python For Loops (`for`, `range()`, `if`)**

This folder contains small Python programs that demonstrate how `for` loops work in Python.

These programs show how to repeat actions, print number sequences, use conditions inside loops, work with lists, and use user input together with loop logic.

---

## What These Programs Do

These programs demonstrate:

• how to repeat code using `for`  
• how to generate sequences with `range()`  
• how to use `if` inside loops  
• how to work with user input  
• how to count and sum values  
• how to loop through words and lists  

The examples gradually become slightly more complex.

---

## 💻 Program 1 — Numbers from 1 to 3

This program prints numbers from 1 to 3.

```python
# Print numbers from 1 to 3
for number in range(1, 4):
    print(f"Number {number}")
```

🔎 Output Preview
```python
Number 1
Number 2
Number 3
```

---

## 💻 Program 2 — Even Numbers to 20

This program prints even numbers from 0 to 18.

```python
# Print even numbers from 0 to 18
for number in range(0, 20, 2):
    print(f"Number {number}")
```

🔎 Output Preview
```python
Number 0
Number 2
Number 4
Number 6
...
Number 18
```

---

## 💻 Program 3 — Print Range by Input

This program asks the user for a number and prints numbers from 0 up to that number.

```python
# Print numbers from 0 up to the entered number
number = int(input("Enter a number: "))

for i in range(number):
    print(i)
```

🔎 Output Preview
```python
Enter a number: 5
0
1
2
3
4
```

---

## 💻 Program 4 — Running Sum from 1 to 10

This program calculates and prints the running sum from 1 to 10.

```python
# Print the running sum from 1 to 10
total = 0

for i in range(1, 11):
    total += i
    print(total)
```

🔎 Output Preview
```python
1
3
6
10
15
...
55
```

---

## 💻 Program 5 — Numbers Before Input

This program asks the user for a number and prints numbers from 1 to one less than that number.

```python
# Print numbers from 1 up to the entered number minus 1
num_input = int(input("Enter a number: "))

for i in range(1, num_input):
    print("Result:", i)
```

🔎 Output Preview
```python
Enter a number: 5
Result: 1
Result: 2
Result: 3
Result: 4
```

---

## 💻 Program 6 — Multiplication Table

This program asks the user for a number and prints its multiplication table.

```python
# Print the multiplication table for the entered number
number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
```

🔎 Output Preview
```python
Enter a number: 3
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
...
3 x 10 = 30
```

---

## 💻 Program 7 — Numbers Divisible by 3

This program prints numbers from 1 to 20 that are divisible by 3.

```python
# Print numbers from 1 to 20 that are divisible by 3
for i in range(1, 21):
    if i % 3 == 0:
        print(i)
```

🔎 Output Preview
```python
3
6
9
12
15
18
```

---

## 💻 Program 8 — Count Numbers Greater Than 5

This program counts how many numbers in the list are greater than 5.

```python
# Count how many numbers in the list are greater than 5
numbers = [1, 5, 8, 2, 10]
count = 0

for n in numbers:
    if n > 5:
        count += 1

print(count)
```

🔎 Output Preview
```python
2
```

---

## 💻 Program 9 — Sum List Numbers

This program calculates the sum of numbers inside a list.

```python
# Calculate the sum of the numbers in the list
total = 0

for num in [10, 20, 30, 40]:
    total += num

print(total)
```

🔎 Output Preview
```python
100
```

---

## 💻 Program 10 — Print Letters

This program asks the user for a word and prints each letter on a new line.

```python
# Print each letter of the entered word on a new line
word = input("Enter a word: ")

for letter in word:
    print(letter)
```

🔎 Output Preview
```python
Enter a word: cat
c
a
t
```

---

## 📂 Files in This Folder

```text
d12_loops_for
│
├── d12_task_01_numbers_1_to_3.py
├── d12_task_02_even_numbers_to_20.py
├── d12_task_03_print_range_by_input.py
├── d12_task_04_running_sum_1_to_10.py
├── d12_task_05_numbers_before_input.py
├── d12_task_06_multiplication_table.py
├── d12_task_07_divisible_by_3.py
├── d12_task_08_count_numbers_greater_than_5.py
├── d12_task_09_sum_list_numbers.py
├── d12_task_10_print_letters.py
└── README.md
```

Each file demonstrates a different way of using `for` loops in Python.
