# Initial balance in ATM
balance = 10000

# Run the loop until user chooses Exit
while True:

    # Display ATM Menu
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    # Take user choice
    choice = int(input("Enter your choice: "))

    # Check current balance
    if choice == 1:
        print("Current Balance = ₹", balance)

    # Deposit money
    elif choice == 2:
        amount = float(input("Enter deposit amount: ₹"))

        # Add amount to balance
        balance = balance + amount

        print("Amount Deposited Successfully")
        print("Updated Balance = ₹", balance)

    # Withdraw money
    elif choice == 3:
        amount = float(input("Enter withdrawal amount: ₹"))

        # Check if balance is sufficient
        if amount <= balance:

            # Deduct amount from balance
            balance = balance - amount

            print("Withdrawal Successful")
            print("Remaining Balance = ₹", balance)

        else:
            print("Insufficient Balance")

    # Exit the program
    elif choice == 4:
        print("Thank You for Using ATM")
        break

    # For invalid menu choice
    else:
        print("Invalid Choice, Please Try Again")