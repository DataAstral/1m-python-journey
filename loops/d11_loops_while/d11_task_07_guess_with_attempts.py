# task_07_guess_with_attempts.py
attempts = 5
while attempts > 0:
    try:
        number_input = int(input("Enter a number: "))
        if number_input == 7:
            print("Correct")
            break
        else:
            attempts -= 1
            print("Try again!")
    except ValueError:
        print("Only numbers are accepted.")
if attempts == 0:
    print("Game over")

   