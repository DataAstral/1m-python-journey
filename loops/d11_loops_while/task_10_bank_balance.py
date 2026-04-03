# task_10_bank_balance.py
balance = 1000

while True:
    print("\n--- BANK MENU ---")
    print("1. Check balance")
    print("2. Deposit money")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print(f"Your balance is: {balance}$")

    elif choice == "2":
        print("Deposit function is under development...")

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Error! Please enter a valid option.")