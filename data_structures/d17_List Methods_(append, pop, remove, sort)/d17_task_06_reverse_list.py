# TASK 6 — REVERSE LIST

original = [10, 20, 30, 40, 50]
reversed_list = []
for i in range(len(original) - 1, -1, -1):
    reversed_list.append(original[i])
print(reversed_list)
