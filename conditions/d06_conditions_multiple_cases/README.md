<p align="center">
  <img src="https://raw.githubusercontent.com/DataAstral/DataAstral/main/banner.png" width="100%">
</p>
# Welcome to DataAstral

One million projects. One path to mastery.

Progress: [░░░░░░░░░░] 0.0001% complete

---

# **🌐** d06_conditions_multiple_cases

## ⚙️ Topic

**Python Conditions (`if`, `elif`, `else`) — Multiple Cases Handling**

This program demonstrates how Python handles multiple conditions using an `if → elif → else` structure, similar to real backend logic.

---

# 🧠 What This Program Does

The program:

1. Stores an HTTP status code.
2. Checks the value using multiple conditions.
3. Uses `elif` to handle several possible cases.
4. Displays different messages depending on the result.
5. Handles unknown cases using `else`.

---

# 💻 Python Code

```python
# HTTP status classification (real backend pattern)

status_code = 404

if status_code == 200:
    print("OK — request successful")
elif status_code == 404:
    print("Not Found — resource not found")
elif status_code == 500:
    print("Server Error — internal server error")
else:
    print(f"Unknown status: {status_code}")
```

---

# 🔎 Output Preview

```python
Not Found — resource not found
```