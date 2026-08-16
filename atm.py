print("Welcome to the ATM")

correct_pin = 123
balance = 1000

pin = int(input("Enter your PIN: "))

if pin == correct_pin:
    print("Welcome to your account")
    print("________ What would you like to do? ________")
    print("1. Check balance")
    print("2. Withdraw")
    print("3. Deposit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(f"Your balance is: {balance}")

    elif choice == 2:
        withdraw_amount = int(input("Enter amount to withdraw: "))

        if withdraw_amount <= balance:
            balance -= withdraw_amount
            print(f"Withdrawal successful! New balance: {balance}")
        else:
            print("Insufficient funds!")

    elif choice == 3:
        deposit_amount = int(input("Enter amount to deposit: "))

        balance += deposit_amount
        print(f"Deposit successful! New balance: {balance}")

    else:
        print("Invalid choice! Please try again.")

else:
    print("Incorrect PIN! Please try again.")
