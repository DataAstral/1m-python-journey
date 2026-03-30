<p align="center">
  <img src="https://raw.githubusercontent.com/DataAstral/DataAstral/main/banner.png" width="100%">
</p>
# Welcome to DataAstral

One million projects. One path to mastery.

Progress: [░░░░░░░░░░] 0.0001% complete

---

# **🎓** d07_conditions_and_logical_operators_and_input

**Python Conditions + Logical Operator (`and`) + User Input**

This program demonstrates how to combine user input with logical conditions to make decisions.

---

#  What This Program Does

The program:

1. Asks the user if they passed the test.
2. Asks if the user arrived on time.
3. Converts input to lowercase using `.lower()`.
4. Uses `and` to check both conditions.
5. Passes the exam only if BOTH answers are "yes".

---

# 💻 Python Code

```python
# Check exam result

# Ask if student passed the test (yes/no)
# Ask if student arrived on time (yes/no)
# If both answers are "yes" → print "Exam passed"
# Otherwise → print "Exam failed"

print("Let's check your results!")

test = input("Did you pass your test (yes/no): ")
on_time = input("Did you arrive on time (yes/no): ")

if test.lower() == "yes" and on_time.lower() == "yes":
    print("Exam passed")
else:
    print("Exam failed")
```

---

# 🔎 Output Preview

```python
Let's check your results!
Did you pass your test (yes/no): yes
Did you arrive on time (yes/no): yes
Exam passed
```

```python
Let's check your results!
Did you pass your test (yes/no): yes
Did you arrive on time (yes/no): no
Exam failed
```