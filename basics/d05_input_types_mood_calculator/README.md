<p align="center">
  <img src="https://raw.githubusercontent.com/DataAstral/DataAstral/main/banner.png" width="100%">
</p>
# Welcome to DataAstral

One million projects. One path to mastery.

Progress: [░░░░░░░░░░] 0.0001% complete

---

# **⌨️** d05_input_types_mood_calculator

## ⚙️ Topic

**Python Input, Data Types, and Simple Logic**

This program demonstrates how to collect user data, process it, and display meaningful output.

---

# 🧠 What This Program Does

The program:

1. Asks the user for personal information (name, age, mood).
2. Collects lifestyle data (coffee intake and sleep hours).
3. Calculates a simple balance between coffee and sleep.
4. Displays a summary of the user’s state.
5. Provides basic advice.

---

# 💻 Python Code

```python
# Ask for the user's name
name = input("Enter your name: ")

# Greet the user
print("Hello " + name)

# Ask for the user's age
age = int(input("Enter your age: "))

# Ask for the user's mood
mood = input("Enter your mood: ")

# Ask for the number of coffee cups
coffee = int(input("Enter how many cups of coffee you had today: "))

# Ask how many hours the user slept
sleep_time = int(input("Enter how many hours you slept: "))

# Calculate balance between coffee and sleep
balance = coffee - sleep_time

# Show results
print("Today you feel", mood)
print("Your age is", age)
print("You drank", coffee, "cups of coffee today")
print("You slept for", sleep_time, "hours")

# Give simple advice
print("Advice: you should get more sleep")
```

---

# 🔎 Output Preview

```python
Enter your name: Anna
Hello Anna
Enter your age: 25
Enter your mood: tired
Enter how many cups of coffee you had today: 3
Enter how many hours you slept: 5

Today you feel tired
Your age is 25
You drank 3 cups of coffee today
You slept for 5 hours
Advice: you should get more sleep
```
