# task_17_separate_types.py
# Given a tuple data.
# Separate numbers and strings into two lists.

data = (1, "two", 3, "four", 5, "six")

numbers = []
strings = []

for i in data:
    if isinstance(i, int):
        numbers.append(i)
    elif isinstance(i, str):
        strings.append(i)

print("Numbers:", *numbers)
print("Strings:", *strings)
