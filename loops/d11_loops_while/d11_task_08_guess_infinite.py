
# task_08_guess_infinite.py
secret_number = 7
while True:
    question = int(input("Try to guess my number: "))
    if question == 7:
        print("You guessed my number is 7")
        break
    elif question > 7:
        print("You guessed too high")
    else:
        print("You guessed too low")
