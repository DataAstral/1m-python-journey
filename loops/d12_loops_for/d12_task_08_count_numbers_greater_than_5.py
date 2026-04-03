# Count how many numbers in the list are greater than 5
numbers = [1, 5, 8, 2, 10]
count = 0

for n in numbers:
    if n > 5:
        count += 1

print(count)
