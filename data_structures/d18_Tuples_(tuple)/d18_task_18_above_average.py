# task_18_above_average.py
# Given a tuple of students and their grades.
# Print students with grades above average.

students = (("Anna", 85), ("Bob", 92), ("Clara", 78), ("Dan", 95), ("Eva", 88))

total = 0
count = 0

for name, grade in students:
    total += grade
    count += 1

average = total / count

for name, grade in students:
    if grade > average:
        print(name, grade)
