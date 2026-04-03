<p align="center">
  <img src="https://raw.githubusercontent.com/DataAstral/DataAstral/main/banner.png" width="100%">
</p>

# Welcome to DataAstral  
One million projects. One path to mastery.  

Progress: [░░░░░░░░░░] 0.0001% complete  

---

## d10_ternary_operator_validation_temperature

**Python Ternary Operator — Input Normalization & Validation**

This program demonstrates how to use a **ternary operator**, `.lower()` normalization, and **input validation**.

---

## What This Program Does

The program:

• asks the user to enter a temperature (hot, warm, cold)  
• converts input to lowercase using `.lower()`  
• uses a **ternary operator** to determine the result  
• in the second version → validates user input  
• prevents invalid values and shows an error message  

---

## 💻 Python Code

```python
# Version 1 — Simple ternary logic
temperature = input("What is the temperature? (hot, warm, cold): ").lower()

result = "Hot" if temperature == "hot" else "Cold" if temperature == "cold" else "Warm"

print(result)


# Version 2 — With validation
temperature = input("What is the temperature? (hot, warm, cold): ").lower()

if temperature in ("hot", "warm", "cold"):
    result = "Hot" if temperature == "hot" else "Cold" if temperature == "cold" else "Warm"
    print(result)
else:
    print("Please enter only: hot, warm, or cold")
```

---

## 🔎 Output Preview

### ✅ Valid input
```
What is the temperature? (hot, warm, cold): hot
Hot
```

### ✅ Valid input (different case)
```
What is the temperature? (hot, warm, cold): COLD
Cold
```

### ❌ Invalid input
```
What is the temperature? (hot, warm, cold): rainy
Please enter only: hot, warm, or cold
```

---

## Key Concept

- `.lower()` → converts input to lowercase  
- `in` → checks if value exists in a group  
- nested ternary → handles multiple conditions  

Example:

```
"Hot" if temperature == "hot" else "Cold" if temperature == "cold" else "Warm"
```

💡 Real-world insight:  
Always validate user input.  
Without validation, your program may give incorrect or misleading results.