<p align="center">
  <img src="https://raw.githubusercontent.com/DataAstral/DataAstral/main/banner.png" width="100%">
</p>

# Welcome to DataAstral

One million projects. One path to mastery.

Progress: [░░░░░░░░░░] 0.0001% complete

---

## d18_Tuples_(tuple)

**Python Tuples**

This folder contains small Python programs that demonstrate how tuples work in Python.

These programs show how to access elements by index, unpack tuples into variables, slice sequences, use built-in functions, filter data with loops, work with nested tuples, and understand why tuples are immutable.

---

## What These Programs Do

These programs demonstrate:

• how to access the first and last element of a tuple  
• how to unpack a tuple into variables  
• how to use `min()`, `max()`, `sum()`, `len()` on tuples  
• how to slice a tuple with `[start:end]`  
• how to use the `.count()` method  
• how to filter elements with a `for` loop and `if`  
• how to reverse a tuple with `[::-1]`  
• how to use `enumerate()` with a custom start  
• how to check types with `isinstance()`  
• how to join tuple elements into a string  
• how tuples are immutable and what happens when you try to change them  
• how nested tuples work  
• how to process a list of tuples  
• how to find min/max without built-ins  
• how to separate elements by type  
• how to calculate an average and filter above-average results  

The examples begin with basic indexing and move toward more complex multi-step logic.

---

### 💻 Program 1 — Favorite Fruits

This program creates a tuple of 5 fruits and prints the first and last element.

```python
fruits = ("apple", "banana", "orange", "mango", "grape")
print(fruits[0], ",", fruits[-1])
```

🔎 Output Preview
```python
apple , grape
```

---

### 💻 Program 2 — Best Friend

This program creates a tuple with a name, last name, and age, then prints only the first and last name.

```python
best_friend = ("Tom", "Stone", 33)
print(best_friend[0], best_friend[1])
```

🔎 Output Preview
```python
Tom Stone
```

---

### 💻 Program 3 — Unpack Person

This program unpacks a tuple into three variables and prints each one.

```python
person = ("Maria", 25, "London")
name, age, city = person
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
```

🔎 Output Preview
```python
Name: Maria
Age: 25
City: London
```

---

### 💻 Program 4 — Numbers Stats

This program prints the minimum, maximum, and sum of a tuple of numbers.

```python
numbers = (3, 7, 1, 9, 4, 6)
print(min(numbers))
print(max(numbers))
print(sum(numbers))
```

🔎 Output Preview
```python
1
9
30
```

---

### 💻 Program 5 — Slicing

This program prints elements at indices 1, 2, 3 using slicing.

```python
colors = ("red", "green", "blue", "yellow", "purple")
print(colors[1:4])
```

🔎 Output Preview
```python
('green', 'blue', 'yellow')
```

---

### 💻 Program 6 — Count Apple

This program counts how many times "apple" appears in a tuple.

```python
words = ("apple", "banana", "cherry", "apple", "cherry", "apple")
print(words.count("apple"))
```

🔎 Output Preview
```python
3
```

---

### 💻 Program 7 — Filter Grades

This program prints only grades above 80.

```python
grades = (75, 90, 88, 62, 95, 71)
for i in grades:
    if i > 80:
        print(i)
```

🔎 Output Preview
```python
90
88
95
```

---

### 💻 Program 8 — Reverse

This program prints all elements of a tuple in reverse order using slicing.

```python
numbers = (4, 8, 15, 16, 23, 42)
print(numbers[::-1])
```

🔎 Output Preview
```python
(42, 23, 16, 15, 8, 4)
```

---

### 💻 Program 9 — Enumerate Cities

This program prints each city with its number starting from 1.

```python
cities = ("Paris", "Berlin", "Rome", "Madrid", "Oslo")
for i, city in enumerate(cities, start=1):
    print(i, city)
```

🔎 Output Preview
```python
1 Paris
2 Berlin
3 Rome
4 Madrid
5 Oslo
```

---

### 💻 Program 10 — Filter Strings

This program prints only the string elements from a mixed tuple.

```python
mixed = (1, "hello", 3.14, True, "world")
for i in mixed:
    if isinstance(i, str):
        print(i)
```

🔎 Output Preview
```python
hello
world
```

---

### 💻 Program 11 — Join Letters

This program joins a tuple of letters into one string separated by "-".

```python
letters = ("a", "b", "c", "d", "e")
result = "-".join(letters)
print(result)
```

🔎 Output Preview
```python
a-b-c-d-e
```

---

### 💻 Program 12 — Average Temperature

This program calculates the average temperature over 7 days.

```python
temps = (22, 19, 25, 30, 17, 28, 21)
total = sum(temps)
result = total / len(temps)
print(result)
```

🔎 Output Preview
```python
23.142857142857142
```

---

### 💻 Program 13 — Immutability

This program tries to change a tuple element and catches the error.

```python
coords = (10, 20)
try:
    coords[0] = 50
except TypeError:
    print("A tuple cannot be changed.")
```

🔎 Output Preview
```python
A tuple cannot be changed.
```

---

### 💻 Program 14 — Nested Team

This program unpacks nested tuples in a loop and prints each person's role.

```python
pythonteam = (("Alice", "developer"), ("Bob", "designer"), ("Clara", "manager"))
for name, job in pythonteam:
    print(f"{name} works as {job}")
```

🔎 Output Preview
```python
Alice works as developer
Bob works as designer
Clara works as manager
```

---

### 💻 Program 15 — Shop Filter

This program prints products from a list of tuples that cost less than 2.0.

```python
pythonshop = [
    ("milk", 1.2),
    ("bread", 0.9),
    ("eggs", 2.5),
    ("butter", 3.1),
    ("juice", 1.8)
]

for item, price in pythonshop:
    if price < 2:
        print(item, price)
```

🔎 Output Preview
```python
milk 1.2
bread 0.9
juice 1.8
```

---

### 💻 Program 16 — Min Max Manual

This program finds the most expensive and cheapest price without using `min()` or `max()`.

```python
prices = (120, 450, 89, 300, 55, 210)

max_price = prices[0]
min_price = prices[0]

for price in prices:
    if price > max_price:
        max_price = price
    if price < min_price:
        min_price = price

print("Most expensive:", max_price)
print("Cheapest:", min_price)
```

🔎 Output Preview
```python
Most expensive: 450
Cheapest: 55
```

---

### 💻 Program 17 — Separate Types

This program separates integers and strings from a mixed tuple into two lists.

```python
data = (1, "two", 3, "four", 5, "six")

numbers = []
strings = []

for i in data:
    if isinstance(i, int):
        numbers.append(i)
    elif isinstance(i, str):
        strings.append(i)

print("Numbers:", *numbers)
print("Strings:", *strings)
```

🔎 Output Preview
```python
Numbers: 1 3 5
Strings: two four six
```

---

### 💻 Program 18 — Above Average

This program calculates the average grade and prints students who scored above it.

```python
students = (("Anna", 85), ("Bob", 92), ("Clara", 78), ("Dan", 95), ("Eva", 88))

total = 0
count = 0

for name, grade in students:
    total += grade
    count += 1

average = total / count

for name, grade in students:
    if grade > average:
        print(name, grade)
```

🔎 Output Preview
```python
Bob 92
Dan 95
Eva 88
```

---

### File List

Each task is saved as a separate file:

• `d18_task_01_fruits.py`  
• `d18_task_02_best_friend.py`  
• `d18_task_03_unpack_person.py`  
• `d18_task_04_numbers_stats.py`  
• `d18_task_05_slicing.py`  
• `d18_task_06_count_apple.py`  
• `d18_task_07_filter_grades.py`  
• `d18_task_08_reverse.py`  
• `d18_task_09_enumerate_cities.py`  
• `d18_task_10_filter_strings.py`  
• `d18_task_11_join_letters.py`  
• `d18_task_12_average_temp.py`  
• `d18_task_13_immutability.py`  
• `d18_task_14_nested_team.py`  
• `d18_task_15_shop_filter.py`  
• `d18_task_16_min_max_manual.py`  
• `d18_task_17_separate_types.py`  
• `d18_task_18_above_average.py`  

---

### How to Run

Run any file separately:

```bash
python d18_task_01_fruits.py
```

