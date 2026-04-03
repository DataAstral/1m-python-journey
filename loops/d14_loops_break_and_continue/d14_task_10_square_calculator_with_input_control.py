# Print the square of positive numbers until the user types "stop"
while True:
    user_input = input("Enter a number (or 'stop'): ")
    if user_input == "stop":
        break
    number = int(user_input)
    if number < 0:
        continue
    print(number ** 2)
