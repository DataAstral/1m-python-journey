<p align="center">
  <img src="https://raw.githubusercontent.com/DataAstral/DataAstral/main/banner.png" width="100%">
</p>

# Welcome to DataAstral

One million projects. One path to mastery.

Progress: [░░░░░░░░░░] 0.0001% complete

---

## d07_conditions_and_logical_operators_and

**Python Conditions + Logical Operator (`and`)**

This program demonstrates how to use the `and` operator to check multiple conditions at the same time.

---

##  What This Program Does

The program:

1. Asks the user if they have a passport.
2. Asks the user if they have a visa.
3. Uses `and` to check both conditions together.
4. Allows travel only if BOTH conditions are true.
5. Denies travel if at least one condition is false.

---

## 💻 Python Code

```python
#  Travel eligibility check

# Ask if the user has a passport
passport = input("Do you have a passport? (yes/no): ")

# Ask if the user has a visa
visa = input("Do you have a visa? (yes/no): ")

# Check both conditions
# If the user has both a passport and a visa → allow travel
if passport == "yes" and visa == "yes":
    print("You can travel abroad!")
# Otherwise → deny travel
else:
    print("You cannot travel.")
```

---

## 🔎 Output Preview

```python
Do you have a passport? (yes/no): yes
Do you have a visa? (yes/no): yes
You can travel abroad!
```

```python
Do you have a passport? (yes/no): yes
Do you have a visa? (yes/no): no
You cannot travel.
```
