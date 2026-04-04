# 10. Search with flag — check if 5 exists
numbers = [2, 4, 6, 8]
found = False

for n in numbers:
    if n == 5:
        found = True
        break

if found:
    print("Found")
else:
    print("Not found")
