
# task_09_guess_with_else.py
attempts = 0
secret_number = 7
while attempts < 5:
    attempts = attempts + 1
    question = int(input("Try to guess my number: "))
    if question == secret_number:
        print("You guessed my number is 7")
        break
    elif question > secret_number:
        print("You guessed too high")
    else:
        print("You guessed too low")
else:
    print("Your attempts are over!")
