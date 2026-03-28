<p align="center">
  <img src="https://raw.githubusercontent.com/DataAstral/DataAstral/main/banner.png" width="100%">
</p>
# Welcome to DataAstral

One million projects. One path to mastery.

Progress: [░░░░░░░░░░] 0.0001% complete

---

# **⌨️** d05_variables_strings_user_card

## ⚙️ Topic

**Python Variables, Strings & Formatting**

This program creates a simple **user card** using variables, string formatting, and basic operations.

---

# 🧠 What This Program Does

The program:

1. Stores user information (name, age, city).
2. Calculates the birth year using the current year.
3. Formats the name into initials.
4. Converts city to uppercase.
5. Generates a username using lowercase.
6. Prints everything in a clean “user card” format.

---

# 💻 Python Code

```python
# Store user information
first_name = "Anna"
last_name = "Smith"
age = 25
city = "London"

# Calculate birth year
current_year = 2025
born = current_year - age

# Print formatted user card
print("=== USER CARD ===")
print(f"Name: {first_name} {last_name[0]}.")   # First name + first letter of last name
print(f"Age: {age}")                          # User age
print(f"City: {city.upper()}")                # City in uppercase
print(f"Born: {born}")                        # Calculated birth year
print(f"Username: {first_name.lower()}_{last_name.lower()}")  # Username format
```

---

# 🔎 Output Preview

```python
=== USER CARD ===
Name: Anna S.
Age: 25
City: LONDON
Born: 2000
Username: anna_smith
```
