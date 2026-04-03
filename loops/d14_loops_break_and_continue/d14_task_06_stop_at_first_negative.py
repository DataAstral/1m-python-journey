# Print numbers until the first negative number appears
numbers_list = [3, 7, 2, -5, 10]

for number in numbers_list:
    if number < 0:
        break
    print(number)
