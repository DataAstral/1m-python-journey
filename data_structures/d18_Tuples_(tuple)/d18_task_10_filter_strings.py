# task_10_filter_strings.py
# Given a tuple mixed = (1, "hello", 3.14, True, "world").
# Print only elements that are strings.

mixed = (1, "hello", 3.14, True, "world")
for i in mixed:
    if isinstance(i, str):
        print(i)
