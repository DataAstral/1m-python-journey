# TASK 9 — UNIQUE ELEMENTS

raw = [1, 2, 2, 3, 4, 4, 4, 5, 1]
unique = []

for n in raw:
    if n not in unique:
        unique.append(n)

print(unique)
