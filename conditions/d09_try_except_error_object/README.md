<p align="center">
  <img src="https://raw.githubusercontent.com/DataAstral/DataAstral/main/banner.png" width="100%">
</p>
# Welcome to DataAstral

One million projects. One path to mastery.

Progress: [░░░░░░░░░░] 0.0001% complete

---

# **🛡️** d09_try_except_error_object

**Python Error Handling (Capturing Exception Object with `as e`)**

This program demonstrates how to catch an error and access its **detailed message** using `as e`.

---

#  What This Program Does

The program:

1. Tries to convert a string `"abc"` into an integer.
2. This causes a `ValueError`.
3. Captures the error using `except ValueError as e`.
4. Prints the **actual error message** from Python.

---

#  Why This Is Important

 This approach allows you to:

- See the **exact error message**
- Understand what went wrong
- Debug your code faster
- Build more **advanced error handling systems**

Instead of just printing a custom message, you can use **real Python error details**.

---

# 💻 Python Code

```python
# Try to convert a string into an integer
try:
    x = int("abc")

# Catch the error and save it into variable 'e'
except ValueError as e:
    # Print the error message
    print(f"Error: {e}")
```

---

# 🔎 Output Preview

```python
Error: invalid literal for int() with base 10: 'abc'
```
