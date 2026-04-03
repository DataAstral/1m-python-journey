# Print only positive numbers from the list
numbers_list = [5, -3, 8, -1, 10]

for number in numbers_list:
    if number < 0:
        continue
    print(number)
