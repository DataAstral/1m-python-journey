<p align="center">
  <img src="https://raw.githubusercontent.com/DataAstral/DataAstral/main/banner.png" width="100%">
</p>

# Welcome to DataAstral

One million projects. One path to mastery.

Progress: [░░░░░░░░░░] 0.0001% complete

---

## d14_loops_break_and_continue

**Python Loop Control (`break`, `continue`, `while True`)**

This folder contains small Python programs that demonstrate how loop control works in Python.

These programs show how to stop loops, skip steps, filter values, work with lists, and build simple interactive loops with user input.

---

## What These Programs Do

These programs demonstrate:

• how to stop a loop using `break`  
• how to skip one step using `continue`  
• how to use `while True` for repeated input  
• how to filter values in a list  
• how to stop when a condition is met  
• how to combine loops with user interaction  

The examples gradually become slightly more complex.

---

## 💻 Program 1 — Stop at Number 7

This program prints numbers from 1 to 10 but stops before 7.

```python
# Print numbers from 1 to 10 but stop before 7
for i in range(1, 11):
    if i == 7:
        break
    print(i)
```

🔎 Output Preview
```python
1
2
3
4
5
6
```

---

## 💻 Program 2 — Skip Number 5

This program prints numbers from 1 to 10 but skips number 5.

```python
# Print numbers from 1 to 10 but skip 5
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
```

🔎 Output Preview
```python
1
2
3
4
6
...
10
```

---

## 💻 Program 3 — Print Only Positive Numbers

This program prints only positive numbers from a list.

```python
# Print only positive numbers from the list
numbers_list = [5, -3, 8, -1, 10]

for number in numbers_list:
    if number < 0:
        continue
    print(number)
```

🔎 Output Preview
```python
5
8
10
```

---

## 💻 Program 4 — Find First Number Greater Than 100

This program finds the first number greater than 100 and stops the loop.

```python
# Print the first number greater than 100
numbers = [10, 50, 120, 30, 200]

for number in numbers:
    if number > 100:
        print(number)
        break
```

🔎 Output Preview
```python
120
```

---

## 💻 Program 5 — Print Only Odd Numbers

This program prints only odd numbers from 1 to 15.

```python
# Print only odd numbers from 1 to 15
for i in range(1, 16):
    if i % 2 == 0:
        continue
    print(i)
```

🔎 Output Preview
```python
1
3
5
7
...
15
```

---

## 💻 Program 6 — Stop at First Negative Number

This program prints numbers from a list until the first negative number appears.

```python
# Print numbers until the first negative number appears
numbers_list = [3, 7, 2, -5, 10]

for number in numbers_list:
    if number < 0:
        break
    print(number)
```

🔎 Output Preview
```python
3
7
2
```

---

## 💻 Program 7 — Infinite Input Loop

This program keeps asking the user for text until the user types `stop`.

```python
# Keep asking for text until the user types "stop"
while True:
    text = input("Enter text (or 'stop'): ")
    if text == "stop":
        break
    print("Here is your text:", text)
```

🔎 Output Preview
```python
Enter text (or 'stop'): hello
Here is your text: hello
Enter text (or 'stop'): stop
```

---

## 💻 Program 8 — Print Words Longer Than 3 Characters

This program prints only words that are longer than 3 characters.

```python
# Print only words longer than 3 characters
words = ["hi", "hello", "ok", "python", "go"]

for w in words:
    if len(w) <= 3:
        continue
    print(w)
```

🔎 Output Preview
```python
hello
python
```

---

## 💻 Program 9 — Find Zero in List

This program looks for `0` in a list and stops when it finds it.

```python
# Find 0 in the list and stop the loop
numbers = [4, 2, 9, 0, 5]

for num in numbers:
    if num == 0:
        print("Here is 0!")
        break
```

🔎 Output Preview
```python
Here is 0!
```

---

## 💻 Program 10 — Square Calculator with Input Control

This program asks the user for numbers, skips negative values, and stops when the user types `stop`.

```python
# Print the square of positive numbers until the user types "stop"
while True:
    user_input = input("Enter a number (or 'stop'): ")
    if user_input == "stop":
        break
    number = int(user_input)
    if number < 0:
        continue
    print(number ** 2)
```

🔎 Output Preview
```python
Enter a number (or 'stop'): 4
16
Enter a number (or 'stop'): -3
Enter a number (or 'stop'): stop
```

---

## 💻 Program 11 — Find Words with Letter "a"

This program prints only words that contain the letter `a`.

```python
# Print only words that contain the letter "a"
words = ["cat", "dog", "apple", "sky", "banana"]

for w in words:
    if "a" in w:
        print(w)
```

🔎 Output Preview
```python
cat
apple
banana
```

---

## 📂 Files in This Folder

```text
d14_loops_break_and_continue
│
├── d14_task_01_stop_at_7.py
├── d14_task_02_skip_number_5.py
├── d14_task_03_print_only_positive_numbers.py
├── d14_task_04_find_first_number_greater_than_100.py
├── d14_task_05_print_only_odd_numbers.py
├── d14_task_06_stop_at_first_negative.py
├── d14_task_07_infinite_input_loop.py
├── d14_task_08_print_words_longer_than_3.py
├── d14_task_09_find_zero_in_list.py
├── d14_task_10_square_calculator_with_input_control.py
├── d14_task_11_find_words_with_letter_a.py
└── README.md
```

Each file demonstrates a different way of controlling loops in Python.
