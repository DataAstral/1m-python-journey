<p align="center">
  <img src="https://raw.githubusercontent.com/DataAstral/DataAstral/main/banner.png" width="100%">
</p>

# Welcome to DataAstral

One million projects. One path to mastery.

Progress: [░░░░░░░░░░] 0.0001% complete

---

## d16_Lists_(list)_Indexing

**Python Lists — Indexing, Slicing, and Search (`list`, `in`, `.index()`, `.count()`)**

This folder contains small Python programs that demonstrate how to work with list indexing and slicing in Python.

These programs show how to access elements by index, slice lists, replace elements, and search inside lists.

---

## What These Programs Do

These programs demonstrate:

• how to access elements using positive and negative indexes  
• how to slice lists to get subsets of elements  
• how to replace an element at a specific index  
• how to check if a value exists in a list with `in`  
• how to find the position of an element with `.index()`  
• how to count occurrences of a value with `.count()`  

The examples gradually become slightly more complex.

---

### 💻 Program 1 — Index Access

This program accesses elements of a list using positive and negative indexes.

```python
# d16_task_01_index_access.py
animals = ["cat", "dog", "parrot", "turtle", "hamster"]

print(animals[1])
print(animals[-1])
print(animals[-2])
```

🔎 Output Preview
```python
dog
hamster
turtle
```

---

### 💻 Program 2 — Slicing

This program slices a list to extract different subsets of numbers.

```python
# d16_task_02_slicing.py
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numbers[:3])
print(numbers[-3:])
print(numbers[3:7])
print(numbers[1::2])
```

🔎 Output Preview
```python
[1, 2, 3]
[8, 9, 10]
[4, 5, 6, 7]
[2, 4, 6, 8, 10]
```

---

### 💻 Program 3 — Replace Element

This program replaces one element in a shopping list and prints the list before and after the change.

```python
# d16_task_03_replace_element.py
shopping = ["bread", "milk", "eggs", "butter"]

print("Before:", shopping)
shopping[1] = "juice"
print("After:", shopping)
```

🔎 Output Preview
```python
Before: ['bread', 'milk', 'eggs', 'butter']
After: ['bread', 'juice', 'eggs', 'butter']
```

---

### 💻 Program 4 — Search and Check

This program checks if a value exists in a list, finds its index, and counts its occurrences.

```python
# d16_task_04_search_and_check.py
scores = [45, 78, 92, 55, 88, 100, 63]

print(100 in scores)
print(scores.index(92))
print(scores.count(55))
```

🔎 Output Preview
```python
True
2
1
```

---

### 📂 Files in This Folder

```text
d16_Lists_(list)_Indexing
│
├── d16_task_01_index_access.py
├── d16_task_02_slicing.py
├── d16_task_03_replace_element.py
├── d16_task_04_search_and_check.py
└── README.md
```

Each file demonstrates a different way of working with list indexing in Python.
