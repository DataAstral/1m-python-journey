# 11. Find maximum in list
numbers = [3, 8, 2, 10, 5]
largest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n

print(largest)
