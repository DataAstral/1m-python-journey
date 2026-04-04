<p align="center">
  <img src="https://raw.githubusercontent.com/DataAstral/DataAstral/main/banner.png" width="100%">
</p>

# Welcome to DataAstral

One million projects. One path to mastery.

Progress: [░░░░░░░░░░] 0.0001% complete

---

## d15_loops_nested_loops

**Python Loops and Nested Loops**

This folder contains small Python programs that demonstrate how regular loops and nested loops work in Python.

These programs show how to print sequences of numbers, use conditions inside loops, calculate sums, search in lists, and build simple text patterns with nested loops.

---

## What These Programs Do

These programs demonstrate:

• how to print numbers in forward and reverse order  
• how to use `if` inside a loop  
• how to skip values with `continue`  
• how to calculate sums and counters  
• how to search for values in lists  
• how to find the maximum value  
• how nested loops work  
• how to print simple patterns and a multiplication table  

The examples begin with basic `for` loops and then move to nested loops.

---

## 💻 Program 1 — Simple Loop

This program prints numbers from 1 to 5.

```python
for i in range(1, 6):
    print(i)
```

🔎 Output Preview
```python
1
2
3
4
5
```

---

## 💻 Program 2 — Reverse Loop

This program prints numbers from 5 to 1.

```python
for i in range(5, 0, -1):
    print(i)
```

🔎 Output Preview
```python
5
4
3
2
1
```

---

## 💻 Program 3 — Even Numbers

This program prints only even numbers from 1 to 10.

```python
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
```

🔎 Output Preview
```python
2
4
6
8
10
```

---

## 💻 Program 4 — Skip Numbers Divisible by 3

This program prints numbers from 1 to 10 but skips numbers divisible by 3.

```python
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)
```

🔎 Output Preview
```python
1
2
4
5
7
8
10
```

---

## 💻 Program 5 — Sum from 1 to 5

This program calculates the sum of numbers from 1 to 5.

```python
total = 0
for i in range(1, 6):
    total += i

print(total)
```

🔎 Output Preview
```python
15
```

---

## 💻 Program 6 — Sum of Even Numbers

This program calculates the sum of even numbers from 1 to 10.

```python
total = 0
for i in range(1, 11):
    if i % 2 == 0:
        total += i

print(total)
```

🔎 Output Preview
```python
30
```

---

## 💻 Program 7 — Count Numbers Greater Than 5

This program counts how many numbers in the list are greater than 5.

```python
numbers = [1, 8, 3, 10, 2]
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

## 💻 Program 8 — Sum of List Elements

This program calculates the sum of all elements in the list.

```python
numbers = [4, 7, 2, 9]
total = 0

for n in numbers:
    total += n

print(total)
```

🔎 Output Preview
```python
22
```

---

## 💻 Program 9 — First Number Greater Than 5

This program finds the first number greater than 5 and stops.

```python
numbers = [2, 4, 7, 9]

for n in numbers:
    if n > 5:
        print(n)
        break
```

🔎 Output Preview
```python
7
```

---

## 💻 Program 10 — Check If 5 Exists

This program checks whether the number `5` is in the list.

```python
numbers = [2, 4, 6, 8]
found = False

for n in numbers:
    if n == 5:
        found = True
        break

if found:
    print("Found")
else:
    print("Not found")
```

🔎 Output Preview
```python
Not found
```

---

## 💻 Program 11 — Find Maximum

This program finds the largest number in the list.

```python
numbers = [3, 8, 2, 10, 5]
largest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n

print(largest)
```

🔎 Output Preview
```python
10
```

---

## 💻 Program 12 — Nested Coordinates

This program uses a nested loop to print coordinate pairs.

```python
for i in range(1, 3):
    for j in range(1, 3):
        print(i, j)
```

🔎 Output Preview
```python
1 1
1 2
2 1
2 2
```

---

## 💻 Program 13 — Square Pattern

This program prints a 3×3 square of stars.

```python
for i in range(3):
    for j in range(3):
        print("*", end="")
    print()
```

🔎 Output Preview
```python
***
***
***
```

---

## 💻 Program 14 — Triangle Pattern

This program prints a triangle of stars.

```python
for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()
```

🔎 Output Preview
```python
*
**
***
****
```

---

## 💻 Program 15 — Mini Multiplication Table

This program prints a small multiplication table.

```python
for i in range(1, 3):
    for j in range(1, 4):
        result = i * j
        print(f"{i} * {j} = {result}")
    print()
```

🔎 Output Preview
```python
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3

2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
```

---

## File List

Each task is also saved as a separate file:

• `task_01_simple_loop.py`  
• `task_02_reverse_loop.py`  
• `task_03_even_numbers.py`  
• `task_04_skip_divisible_by_3.py`  
• `task_05_sum_1_to_5.py`  
• `task_06_sum_even_numbers.py`  
• `task_07_count_greater_than_5.py`  
• `task_08_sum_list_elements.py`  
• `task_09_first_greater_than_5.py`  
• `task_10_find_number_5.py`  
• `task_11_find_maximum.py`  
• `task_12_nested_coordinates.py`  
• `task_13_square_pattern.py`  
• `task_14_triangle_pattern.py`  
• `task_15_mini_multiplication_table.py`  

---

## How to Run

Run any file separately:

```bash
python task_01_simple_loop.py
```

