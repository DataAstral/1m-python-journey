<p align="center">
  <img src="https://raw.githubusercontent.com/DataAstral/DataAstral/main/banner.png" width="100%">
</p>

# Welcome to DataAstral  
One million projects. One path to mastery.  

Progress: [░░░░░░░░░░] 0.0001% complete  

---

## d10_ternary_operator_multiple_conditions

**Python Ternary Operator — Multiple Conditions**

This program demonstrates how to use a **ternary operator with multiple conditions** in one line.

---

## What This Program Does

The program:

• asks the user to enter their mood  
• checks if the mood is "happy", "sad", or something else  
• uses **nested ternary operators** for multiple conditions  
• assigns the correct result based on the input  
• prints the final mood  

---

## 💻 Python Code

```python
# Ask user for mood
mood = input("What is your mood?: (happy, sad, ok): ")

# Use nested ternary operator for multiple conditions
result = "happy" if mood == "happy" else "sad" if mood == "sad" else "ok"

# Print result
print(f"Your mood is {result}")
```

---

## 🔎 Output Preview

### ✅ Happy
```
What is your mood?: happy
Your mood is happy
```

### 😢 Sad
```
What is your mood?: sad
Your mood is sad
```

### 😐 Other input
```
What is your mood?: tired
Your mood is ok
```

---

## Key Concept

- you can chain multiple conditions in a ternary operator  
- structure:

```
value1 if condition1 else value2 if condition2 else value3
```

Example:

```
"happy" if mood == "happy" else "sad" if mood == "sad" else "ok"
```

⚠️ Important:  
Nested ternary operators can become hard to read.  
In real projects, developers often prefer `if / elif / else` for clarity.