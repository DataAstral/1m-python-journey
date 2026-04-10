<p align="center">
  <img src="https://raw.githubusercontent.com/DataAstral/DataAstral/main/banner.png" width="100%">
</p>

# Welcome to DataAstral

One million projects. One path to mastery.

Progress: [░░░░░░░░░░] 0.0001% complete

---

## d17_List Methods_(append, pop, remove, sort)

**Python List Methods (`append`, `pop`, `remove`, `sort`, `len`, `sum`, `max`)**

This folder contains small Python programs that demonstrate how to use the most common list methods in Python.

These programs show how to add, remove, and sort elements, combine multiple methods, filter values, work with nested lists, and find unique or extreme values.

---

## What These Programs Do

These programs demonstrate:

• how to add elements to a list with `.append()`  
• how to remove the last element with `.pop()`  
• how to remove a specific value with `.remove()`  
• how to sort a list in place with `.sort()`  
• how to combine multiple list methods in one program  
• how to reverse a list using a loop  
• how to filter elements by condition  
• how to work with nested 2D lists  
• how to collect unique elements  
• how to find the second largest value  

The examples begin with basic methods and gradually become more complex.

---

### 💻 Program 1 — Append

This program adds a new element to the end of a list using `.append()`.

```python
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)
```

🔎 Output Preview
```python
[1, 2, 3, 4]
```

---

### 💻 Program 2 — Pop

This program removes the last element from a list using `.pop()`.

```python
numbers = [5, 6, 7]
numbers.pop()
print(numbers)
```

🔎 Output Preview
```python
[5, 6]
```

---

### 💻 Program 3 — Remove

This program removes a specific value from a list using `.remove()`.

```python
numbers = [10, 20, 30]
numbers.remove(20)
print(numbers)
```

🔎 Output Preview
```python
[10, 30]
```

---

### 💻 Program 4 — Sort

This program sorts a list of numbers in ascending order using `.sort()`.

```python
numbers = [8, 3, 1, 5]
numbers.sort()
print(numbers)
```

🔎 Output Preview
```python
[1, 3, 5, 8]
```

---

### 💻 Program 5 — Combined Methods

This program chains multiple list methods together and prints the result with its count and sum.

```python
numbers = [7, 2, 9, 7, 4, 1, 10, 2]
numbers.remove(7)
numbers.append(6)
numbers.sort()
numbers.pop()
print("New list:", numbers)
print("Count:", len(numbers))
print("Sum:", sum(numbers))
```

🔎 Output Preview
```python
New list: [1, 2, 2, 4, 6, 7, 9]
Count: 7
Sum: 31
```

---

### 💻 Program 6 — Reverse List

This program reverses a list manually using a loop and `.append()`.

```python
original = [10, 20, 30, 40, 50]
reversed_list = []
for i in range(len(original) - 1, -1, -1):
    reversed_list.append(original[i])
print(reversed_list)
```

🔎 Output Preview
```python
[50, 40, 30, 20, 10]
```

---

### 💻 Program 7 — Filter Big Numbers

This program filters numbers greater than 10 into a new list.

```python
numbers = [3, 17, 8, 42, 5, 99, 21, 6]
big = []
for n in numbers:
    if n > 10:
        big.append(n)
print(big)
```

🔎 Output Preview
```python
[17, 42, 99, 21]
```

---

### 💻 Program 8 — Nested List (2D Grid)

This program works with a 2D grid stored as a nested list and prints specific elements and rows.

```python
grid = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print(grid[1][2])
print(grid[1])
print(grid[-1][-1])

for row in grid:
    for el in row:
        print(el)
```

🔎 Output Preview
```python
7
[5, 6, 7, 8]
12
1
2
3
...
12
```

---

### 💻 Program 9 — Unique Elements

This program removes duplicates from a list by collecting only unique values.

```python
raw = [1, 2, 2, 3, 4, 4, 4, 5, 1]
unique = []

for n in raw:
    if n not in unique:
        unique.append(n)

print(unique)
```

🔎 Output Preview
```python
[1, 2, 3, 4, 5]
```

---

### 💻 Program 10 — Second Max

This program finds the second largest value in a list without sorting.

```python
nums = [3, 7, 1, 9, 4, 6, 9, 2]

first_max = max(nums)
second_max = None

for n in nums:
    if n == first_max:
        continue
    if second_max is None or n > second_max:
        second_max = n

print(second_max)
```

🔎 Output Preview
```python
7
```

---

### File List

Each task is saved as a separate file:

• `d17_task_01_append.py`  
• `d17_task_02_pop.py`  
• `d17_task_03_remove.py`  
• `d17_task_04_sort.py`  
• `d17_task_05_combined_methods.py`  
• `d17_task_06_reverse_list.py`  
• `d17_task_07_filter_big_numbers.py`  
• `d17_task_08_nested_list.py`  
• `d17_task_09_unique_elements.py`  
• `d17_task_10_second_max.py`  

---

### How to Run

Run any file separately:

```bash
python d17_task_01_append.py
```

Or open `main.py` to see all examples together.
